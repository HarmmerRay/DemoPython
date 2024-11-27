import os
import subprocess
import traceback
import uuid

from moviepy.video.io.VideoFileClip import VideoFileClip

from zhixuan_ai_test.db import dao


def get_done_video2(url,name):
    video_path = '99个视频/' + str(name) + '.mp4'

    # 检查视频文件是否已存在
    if os.path.exists(video_path) and os.path.isfile(video_path):
        print(f"文件已存在: {video_path}")
    else:
        # 如果不存在，尝试下载视频
        try:
            import wget
            video_path = '99个视频/' + str(name) + '.mp4'
            wget.download(url, video_path)
        except Exception as e:
            print(traceback.format_exc())
            return None, None

if __name__ == '__main__':
    url_list = dao.query2("select url from list where publish_time='2024-11-27' order by id asc limit 752")
    num = 95
    count = 1
    for url in url_list:
        try:
            print(str(count) + ":" + url['url'])
            count += 1
            cmd = "ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 -i %s" % \
                  url['url']
            result = float(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT,timeout=10).decode('utf-8').strip())
            # print("Video duration:", result)
            if result > 20 or result < 10:
                continue
        except Exception as e:
            print(e)
            print(url['url'] + "不是视频")
            continue
        get_done_video2(url['url'],num)
        print(num)
        num += 1

