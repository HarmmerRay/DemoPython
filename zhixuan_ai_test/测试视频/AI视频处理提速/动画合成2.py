import os
import random

from moviepy.video.io.VideoFileClip import VideoFileClip


def add_donghua_ffmpeg(input_video,donghua,donghua_pos,visible=True):
    video_clip = VideoFileClip(input_video)
    duration = video_clip.duration
    video_fps = video_clip.fps
    donghua_clip = VideoFileClip(donghua)
    donghua_duration = donghua_clip.duration
    # 随机动画开始时间戳
    d_start = round(random.uniform(0, donghua_duration-8), 2)
    print("设置动画开始时间:", d_start)
    d_duration = round(donghua_duration - d_start,2)
    print("截取后的动画持续时间:",d_duration)
    # 动画素材输出
    donghua_output = "./tmp_video/" + str(d_duration) + donghua.split("/")[-1]
    print("dealed_donghua_path",donghua_output)
    random_cmd = f"""ffmpeg -loglevel quiet -i %s -ss %s -t %s -c copy -y %s """ % (donghua, d_start, d_duration,donghua_output)
    os.system(random_cmd)
    # 截取动画下半部分的，x轴前半段中间位置到x轴后半段中间位置的动画区域
    crop_h = donghua_clip.size[1] * 0.3
    crop_w = donghua_clip.size[0] * 0.4
    if visible:
        print("-------------------添加动画的视频路径",input_video,"它的视频时长为：",duration)
        output_video = "./tmp_video/" + input_video.split("/")[-1] + ".donghua.avi"
        if donghua_pos == "fullscreen":
            print("设置透明动画在视频全屏")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "top":
            print("设置透明动画在视频顶部")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=0:y=H*-0.8:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "bottom":
            print("设置透明动画在视频底部")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=0:y=H*0.8:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "topBottom":
            print("设置透明动画在视频上下方")
            #  设置动画的fps跟原视频的fps相同   可能不用
            # 动画添加不可
            ffmpeg_cmd = f"""ffmpeg -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -stream_loop -1 -i {donghua_output}  -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=0:y=H*-0.8:eof_action=repeat:enable='lte(t,30)'[av];[2:v]fps={video_fps}[ov2];[av][ov2]overlay=x=0:y=H*0.8:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "topLeft":
            print("设置透明动画在视频左上角")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1,scale=iw*1.2:ih*1.2,crop={crop_w}:{crop_h}:iw*1.2*1/4:ih/3[ov];[1:v][ov]overlay=x=0:y=0:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "topRight":
            print("设置透明动画在视频右上角")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1,scale=iw*1.2:ih*1.2,crop={crop_w}:{crop_h}:iw*1.2*1/4:ih/3[ov];[1:v][ov]overlay=x=W-w:y=0:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "bottomLeft":
            print("设置透明动画在视频左下角")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1,scale=iw*1.2:ih*1.2,crop={crop_w}:{crop_h}:iw*1.2*1/4:ih/3[ov];[1:v][ov]overlay=x=0:y=H-h:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        elif donghua_pos == "bottomRight":
            print("设置透明动画在视频右下角")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1,scale=iw*1.2:ih*1.2,crop={crop_w}:{crop_h}:iw*1.2*1/4:ih/3[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        else:
            print("默认全屏")
            ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=argb,fps={video_fps},fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,30)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        print("添加动画执行的命令:",ffmpeg_cmd)
        os.system(ffmpeg_cmd)
    else:
        print("-------------------添加防重叠动画的视频",input_video,"它的视频时长为：",duration)
        output_video = "./tmp_video/" + input_video.split("/")[-1] + ".invis.avi"
        ffmpeg_cmd = f"""$FFMPEG_BINARY -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=rgba,fps={video_fps},colorchannelmixer=aa=0.001,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,10)'" -map 1:a? -c:v rawvideo -c:a aac -pix_fmt yuv420p -preset ultrafast -t {duration} -y {output_video}"""
        print("添加防重动画执行的命令:",ffmpeg_cmd)
        os.system(ffmpeg_cmd)
    return output_video

if __name__ == '__main__':
    add_donghua_ffmpeg("555.mp4","./sucai/mov/xingxingfuxian.mov","topBottom",True)