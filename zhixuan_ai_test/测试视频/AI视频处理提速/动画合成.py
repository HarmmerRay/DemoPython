import datetime
import os

# cmd = """ffmpeg -i input.mp4 -i xiayu.mov -filter_complex "[1:v]loop=loop=-1,setpts=N/(FRAME_RATE*TB)[transparent]; [0:v][transparent]overlay=x=W-w:y=H-h" -c:v libx264 -pix_fmt yuv420p -preset ultrafast -y output.avi"""

# cmd = """ffmpeg -stream_loop -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb[ov];[1:v][ov]overlay=0:0:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t $(ffprobe -v error -show_entries format=duration -of csv=p=0 input.mp4) output.mp4"""
# print(cmd)
# os.system(cmd)


import os

# Step 1: 使用 ffprobe 获取 input.mp4 的时长
pipe = os.popen("ffprobe -v error -show_entries format=duration -of csv=p=0 %s" % "yuan.mp4")
duration = float(pipe.read().strip())
print(duration)
# Step 2: 拼接 ffmpeg 命令字符串
start_time = datetime.datetime.now()
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat" -map 1:a -c:a copy -c:v hevc_nvenc -pix_fmt yuv420p -t {duration} -y output.mp4"""
# 随机开头帧
# random_cmd = f"""ffmpeg -i %s -ss %s -t %s -vf "crop=100:100:100:100" -c:v prores_ks -profile:v 3 -pix_fmt yuv422p10le %s """ % ("xiayu.mov", 2,5,"2" + "xiayu.mov")
# os.system(random_cmd)
# pipe = os.popen("ffprobe -v error -show_entries format=duration -of csv=p=0 %s" % "1" + "xiayu.mov")
# duration = float(pipe.read().strip())# print(duration)
# 全屏
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i 8_59s.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,30)'" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i 8_59s.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat:enable='lte(t,30)'" -map 1:a -c:a copy -c:v h264_nvenc -pix_fmt yuv420p -preset slow -t {duration} -y output.mp4""" # hevc_nvenc avi_nvenc
# 顶部
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=0:y=H*-0.8:eof_action=repeat:enable='lte(t,60)'" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# 底部
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=0:y=H*0.8:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# 上下方
ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i yuan.mp4 -i xiayu.mov -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1[ov];[1:v][ov]overlay=x=0:y=H*-0.8:eof_action=repeat[av];[av][2:v]overlay=x=0:y=H*0.8:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# 左上角
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1,scale=iw*1.5:ih*1.5,crop=1080*0.2:1920*0.2:1080*0.2:1920*0.2[ov];[1:v][ov]overlay=x=0:y=0:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# 右上角
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1,scale=iw*1.5:ih*1.5,crop=1080*0.2:1920*0.2:iw/4:ih/2[ov];[1:v][ov]overlay=x=W-w:y=0:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# 左下角
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1,scale=iw*1.5:ih*1.5,crop=1080*0.2:1920*0.2:iw/4:ih/2[ov];[1:v][ov]overlay=x=0:y=H-h:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""
# 右下角
# ffmpeg_cmd = f"""ffmpeg -stream_loop -1 -i xiayu.mov -i input.mp4 -filter_complex "[0:v]format=argb,fade=in:st=0:d=1:alpha=1,scale=iw*1.5:ih*1.5,crop=1080*0.2:1920*0.2:iw/4:ih/2[ov];[1:v][ov]overlay=x=W-w:y=H-h:eof_action=repeat" -map 1:a -c:a copy -c:v rawvideo -pix_fmt yuv420p -preset ultrafast -t {duration} -y output.avi"""

print("执行的cmd命令:",ffmpeg_cmd)
os.system(ffmpeg_cmd)
#
end_time = datetime.datetime.now()
print("开始时间:",start_time.strftime("%Y-%m-%d %H:%M:%S"),"结束时间:",end_time.strftime("%Y-%m-%d %H:%M:%S"),"执行耗时:",(end_time - start_time).seconds)