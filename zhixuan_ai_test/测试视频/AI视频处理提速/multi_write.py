import os
import subprocess
import threading
import time

from moviepy.video.io.VideoFileClip import VideoFileClip

video_path = "./eesw-降温啦.mp4"
mov_path = "D:\Desktop\zhixuan_ai\ai_video\sucai\mov\luoye.mov"
video_clip = VideoFileClip(video_path)

def multi_write(video_clip,final_name):
    video_duration = int(video_clip.duration)
    def split_video(clip,start_time,end_time,video_name):
        subclip = clip.subclip(start_time,end_time)
        subclip.write_videofile(video_name,codec="rawvideo", threads=8, ffmpeg_params=['-pix_fmt', 'yuv420p', '-preset','ultrafast'])
    threads = []
    video_names = []
    for i in range(0,video_duration,2):
        start_time = i
        end_time = min(i + 2, video_duration)
        video_name = final_name + "." + str(i) + "clip.final.avi"
        video_names.append(video_name)
        print("正在写入子视频:",video_name)
        thread = threading.Thread(target=split_video,args=(video_clip,start_time,end_time,video_name))
        threads.append(thread)
        thread.start()
        time.sleep(1)
    for thread in threads:
        thread.join()
    print("所有的子视频已生成完毕")
    with open("videos_list.txt","w") as f:
        for name in video_names:
            f.write("file " + name+"\n")
    final_name = final_name + ".final.avi"
    subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "videos_list.txt", "-c", "copy", final_name])
    # os.remove("videos_list.txt")
    # for name in video_names:
    #     os.remove(name)
    print("所有子视频已合并为一个文件，final_video已经生成",final_name)
multi_write(video_clip,"./aaa")