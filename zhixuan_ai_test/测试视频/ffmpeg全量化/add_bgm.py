import os

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

add_bgm_ffmpeg("1.mp3","2.mp4")