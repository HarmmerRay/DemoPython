"""ffmpeg -i input.mp4 -i xiayu.mov -filter_complex  "[1:v]format=rgba,colorchannelmixer=aa=1[transparent];  [0:v][transparent]overlay=x=W-w:y=H-h:shortest=1" -c:v rawvideo -pix_fmt yuv420p -preset ultrafast  output.avi"""
from moviepy.video.io.VideoFileClip import VideoFileClip

clip = VideoFileClip("./eesw-降温啦.mp4")
print(type(clip.duration))