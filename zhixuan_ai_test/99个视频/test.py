import os

if __name__ == "__main__":
    for i in range(2, 51):
        input_video = "1aa.mp4"
        output_video ="tmp_video/" + str(i) + "_1aa.avi"
        donghua_output = str(i) + ".mp4"
        ffmpeg_cmd = f"""ffmpeg -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=rgba,fps=30,colorchannelmixer=aa=0.01,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,10)'" -map 1:a? -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t 7.67 -y {output_video}"""
        # ffmpeg_cmd = f"""ffmpeg -loglevel quiet -stream_loop -1 -i {donghua_output} -i {input_video} -filter_complex "[0:v]format=rgba,fps=30,colorchannelmixer=aa=0.01,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,10)'" -map 1:a? -c:v libx264 -t 7.67 -y {output_video}"""
        print("添加防重动画执行的命令:", ffmpeg_cmd)
        os.system(ffmpeg_cmd)