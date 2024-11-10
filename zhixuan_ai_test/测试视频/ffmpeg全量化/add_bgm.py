import os
import subprocess

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


def add_bgm_ffmpeg(bgm_path,input_video,volume_factor=0.5,fade_duration=3):
    process_bgm = bgm_path + ".proc.mp3"
    output_video = input_video + ".bgm.avi"
    # 获取视频时长
    video_duration = float(VideoFileClip(input_video).duration)

    # 获取背景音乐时长
    bgm_duration = float(AudioFileClip(bgm_path).duration)
    fade_out = bgm_duration - fade_duration
    # 处理背景音乐
    bgm_cmd = f"""ffmpeg -i "{bgm_path}" -af "volume={volume_factor},afade=in:st=0:d={fade_duration},afade=out:st={fade_out}:d={fade_duration}" -t {video_duration} -y "{process_bgm}" """
    print(bgm_cmd)
    os.system(bgm_cmd)
    # 混合音频并生成最终视频
    video_cmd = f"""ffmpeg -i {input_video} -i {process_bgm} -filter_complex "[0:a][1:a]amix=inputs=2:duration=longest" -c:v rawvideo -c:a aac -y {output_video}"""
    print(video_cmd)
    os.system(video_cmd)
    return output_video
def combine_tou_wei(org_path,piantou_path,pianwei_path,crf_val=12):
    output_path = org_path + ".connect.mp4"
    command = ['ffmpeg',]
    output_command = ['-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-c:a', 'aac', '-crf', str(crf_val), '-y',output_path]
    org_width,org_height = VideoFileClip(org_path).size
    piantou_width,piantou_height = VideoFileClip(piantou_path).size
    pianwei_width,pianwei_height = VideoFileClip(pianwei_path).size
    if org_width < org_height:
        print("竖屏视频")
        # 片头片尾按照原视频宽度适配
        if piantou_path and pianwei_path:
            print("添加片头+片尾")
            input_command = ["-i",piantou_path,"-i",org_path,"-i",pianwei_path]
            filter_command = ['-filter_complex',f"""[0:v]scale={org_width}:-1,pad={org_width}:{org_height}:0:({org_height}-ih)/2,setsar=1[v0]; [1:v]scale={org_width}:{org_height},setsar=1[v1]; [2:v]scale={org_width}:-1,pad={org_width}:{org_height}:0:({org_height}-ih)/2,setsar=1[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1[v][a]""",]
        elif piantou_path:
            print("添加片头")
            input_command = ["-i",piantou_path,"-i",org_path]
            filter_command = ['-filter_complex',f"""[0:v]scale={org_width}:-1,pad={org_width}:{org_height}:0:({org_height}-ih)/2,setsar=1[v0]; [1:v]scale={org_width}:{org_height},setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]""",]
        elif pianwei_path:
            print("添加片尾")
            input_command = ["-i", org_path, "-i", pianwei_path]
            filter_command = ['-filter_complex',f"""[0:v]scale={org_width}:{org_height},setsar=1[v0]; [1:v]scale={org_width}:-1,pad={org_width}:{org_height}:0:({org_height}-ih)/2,setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=0:a=0[v][a]""",]
        else:
            print("没有设置添加片头片尾，返回原视频")
            return org_path
    else:
        print("横屏视频")
        # 原视频按照片头片尾宽度
        if piantou_path and pianwei_path:
            print("添加片头+片尾")
            input_command = ["-i", piantou_path, "-i", org_path, "-i", pianwei_path]
            if piantou_width < piantou_height:
                filter_command = ['-filter_complex',f"""[0:v]scale={piantou_width}:{piantou_height},setsar=1[v0]; [1:v]scale={piantou_width}:-1,pad={piantou_width}:{piantou_height}:0:({piantou_height}-ih)/2,setsar=1[v1]; [2:v]scale={piantou_width}:-1,pad={piantou_width}:{piantou_height}:0:({piantou_height}-ih)/2,setsar=1[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1[v][a]""", ]
            elif pianwei_width < pianwei_height:
                filter_command = ['-filter_complex',f"""[0:v]scale={pianwei_width}:-1,pad={pianwei_width}:{pianwei_height}:0:({pianwei_height}-ih)/2,setsar=1[v0]; [1:v]scale={pianwei_width}:-1,pad={pianwei_width}:{pianwei_height}:0:({pianwei_height}-ih)/2,setsar=1[v1]; [2:v]scale={pianwei_width}:-1,setsar=1[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1[v][a]""", ]
            else:
                filter_command = ['-filter_complex',f"""[0:v]scale={org_width}:-1,setsar=1[v0]; [1:v]scale={org_width}:{org_height},setsar=1[v1]; [2:v]scale={org_width}:-1,setsar=1[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1[v][a]""", ]
        elif piantou_path:
            print("添加片头")
            input_command = ["-i", piantou_path, "-i", org_path]
            if piantou_width < piantou_height:
                filter_command = ['-filter_complex',f"""[0:v]scale={piantou_width}:{piantou_height},setsar=1[v0]; [1:v]scale={piantou_width}:-1,pad={piantou_width}:{piantou_height}:0:({piantou_height}-ih)/2,setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]""", ]
            else:
                filter_command = ['-filter_complex',f"""[0:v]scale={org_width}:-1,setsar=1[v0]; [1:v]scale={org_width}:{org_height},setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]""", ]
        elif pianwei_path:
            print("添加片尾")
            input_command = ["-i", org_path, "-i", pianwei_path]
            if pianwei_width < pianwei_height:
                filter_command = ['-filter_complex',f"""[0:v]scale={pianwei_width}:-1,pad={pianwei_width}:{pianwei_height}:0:({pianwei_height}-ih)/2,setsar=1[v0]; [1:v]scale={pianwei_width}:{pianwei_height},setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=0:a=0[v][a]""", ]
            else:
                filter_command = ['-filter_complex',f"""[0:v]scale={org_width}:-1,setsar=1[v0]; [1:v]scale={org_width}:-1,setsar=1[v1]; [v0][0:a][v1][1:a]concat=n=2:v=0:a=0[v][a]""", ]
        else:
            print("没有设置添加片头片尾，返回原视频")
            return org_path
        # 片头片尾按照原视频高度适配
    command = command + input_command + filter_command + output_command
    print(command)
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Connect video generating False: {result.stderr}")
        return org_path
    else:
        print("Connect video generated successfully")
        return output_path

# 竖屏+竖屏 过
# combine_tou_wei('2.mp4', '1.mp4', '1.mp4')
# ffmpeg -loglevel quiet -i 1.mp4 -i 2.mp4 -i 1.mp4 -filter_complex "[0:v]scale=1080:-1,setsar=1[v0]; [1:v]scale=1080:1920,setsar=1[v1]; [2:v]scale=1080:-1,setsar=1[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1[v][a]" -map "[v]" -map "[a]" output.mp4
# 横屏+头竖屏 过
# combine_tou_wei('zimu1.mp4', '1.mp4', 'zimu1.mp4')
# 横屏+尾竖屏 过
# combine_tou_wei('zimu1.mp4', 'zimu1.mp4', '1.mp4')
# 横屏+头尾竖屏 过
# combine_tou_wei('demo.mp4', '1.mp4', '1.mp4')
# ffmpeg -i 1.mp4 -i zimu1.mp4 -i 1.mp4 -filter_complex "[0:v]scale=-1:1920,setsar=1[v0]; [1:v]setsar=1[v1]; [2:v]scale=-1:1920,setsar=1[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1[v][a]" -map "[v]" -map "[a]" output_heng.mp4
# 横屏＋横屏 过
# combine_tou_wei('zimu1.mp4', 'zimu1.mp4', 'demo.mp4')

# 竖屏+横屏 过
# combine_tou_wei('1.mp4', 'demo.mp4', 'demo.mp4')
# 竖屏+头横屏 过
# combine_tou_wei('1.mp4', 'demo.mp4', '1.mp4')
# 竖屏+尾横屏 过
# combine_tou_wei('2.mp4', '1.mp4', 'demo.mp4')
# combine_tou_wei("1.mp4","2.mp4","1.mp4")
# add_bgm_ffmpeg("1.mp3","2.mp4")

# ffmpeg -i 2.mp3 -stream_loop -1 -i 1.mp3 -t {audio_duration} -filter_complex "amix=inputs=2" -c:a aac -y output.mp3
# def stack_audio_bgm(org_audio,bgm_audio,volume_factor=0.5):
#     audio_duration = AudioFileClip(org_audio).duration
#     fadout_time = audio_duration - 3
#     audio_output = org_audio + ".stack.mp3"
#     cmd = f"""ffmpeg -i {org_audio} -stream_loop -1 -i {bgm_audio} -t {audio_duration} -filter_complex "[1:a]volume={volume_factor},afade=t=in:st=0:d=3,afade=t=out:st={fadout_time}:d=3[a1];[0:a][a1]amix=inputs=2" -y {audio_output}"""
#     print(cmd)
#     os.system(cmd)
#     return audio_output
# stack_audio_bgm("2.mp3","1.mp3")
# def add_bgm_ffmpeg(bgm_path,input_video,volume_factor=0.5):
#     process_bgm = bgm_path + ".proc.mp3"
#     output_video = input_video + ".bgm.avi"
#     # 获取视频时长
#     video_duration = float(VideoFileClip(input_video).duration)
#     fadeout_time = video_duration - 3
#     # 混合音频并生成最终视频
#     video_cmd = f"""ffmpeg -i {input_video} -stream_loop -1 -i {process_bgm} -t {video_duration} -filter_complex "[1:a]volume={volume_factor},afade=t=in:st=0:d=3,afade=t=out:st={fadeout_time}:d=3[a1];[0:a][a1]amix=inputs=2" -c:v rawvideo -c:a aac -y {output_video}"""
#     print(video_cmd)
#     os.system(video_cmd)
#     return output_video
# add_bgm_ffmpeg("1.mp3","1.mp4")
def replace_org_audio(org_path, audio_path):
    video_duration = VideoFileClip(org_path).duration
    output_path = org_path + ".replace.avi"
    cmd = f"""ffmpeg -i {org_path} -i {audio_path} -t {video_duration} -c:v rawvideo -c:a aac -map 0:v:0 -map 1:a:0 -y {output_path}"""
    print(cmd)
    os.system(cmd)
    return output_path
replace_org_audio("demo1.mp4","1.mp3")