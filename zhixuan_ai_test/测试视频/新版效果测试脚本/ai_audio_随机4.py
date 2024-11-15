import os
import random
import subprocess
import traceback

import requests
import json

from moviepy.video.VideoClip import VideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from zhixuan_ai_test.db import dao


# 示例数据，假设你有20条数据
data = {
        "titles":{"title1":"66666","title2":"智选AI带货系统","title3":"网友：有这好东西？怎么不早告诉我"},
        "info": {
        }
    }
fix_info = {
            "clean_info": 1,
            "visible_texture_pos": "topBottom",
            "visible_texture_id": 0,
            "add_bgm_id": 0,
            "yinse_id": 0,
            "add_closing_id": 3,
            "add_opening_id": 7484
        }
keys = [
        "up_bottom_cover",
        "change_face",
        "visible_texture",
        "up_short_title",
        "up_comment",
        "ai_audio",
        "cover_caption",
        "add_bgm",
        "add_opening",
        "add_closing",
        "change_frame_order"
    ]
# data['info'] = {key: random.randint(0, 1) for key in keys}
data['info'] = {key: 1 for key in keys}
for i in fix_info:
    data['info'][i] = fix_info[i]

url_list = dao.query2("select url from list order by id asc limit 100")

# url_list = ['https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/5668eda3-91d8-11ef-aa54-84959735d760.mp4',
#             'https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/c55ecca0-91d8-11ef-b91b-84959735d760.mp4',
#             'https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/03fe513b-91d9-11ef-9b42-84959735d760.mp4']
# # 请求地址
# url2 = "http://127.0.0.1:5000/new_deal"
url2 = "http://152.136.33.202:8080/new_deal"

visible_texture_pos = ['topLeft','topRight','bottomLeft','bottomRight','fullscreen', 'top', 'bottom', 'topBottom']
# 循环发送20个POST请求
num = 0
for url in url_list:
    # url = {'url':url}
    if num >= 16:
        break
    try:
        VideoFileClip(url['url'])
    except Exception as e:
        # print(traceback.format_exc())
        print(url['url']+"不是视频")
        continue
    try:

        cmd = "ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 -i %s" % url['url']
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8').strip()
        print("Video duration:", result)
        print(url['url'])
        if float(result) > 60.0:
            continue
        data['url'] = str(url['url'])
        data['visible_texture_pos'] = visible_texture_pos[num % 5]
        num += 1
        print(data)
        response = requests.post(url2, json=data, timeout=3600)  # 设置等待时长为1小时
        print(f"Request {url} sent successfully.")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.json()}\n\n")
        # 将响应内容写入文件，一行一行追加
        with open("all_responses4.txt", "a", encoding="utf-8") as file:
            file.write(f"Response content: {json.dumps(response.json(), ensure_ascii=False)}\n")
    except requests.exceptions.RequestException as e:
        print(f"Request {url} failed: {e}")

# https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/d02dd4c7-8799-11ef-93ca-84959735d760.mp4
# https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/d02dd4c7-8799-11ef-93ca-84959735d760.mp4
# url_list = dao.query2("select url from list order by id desc limit 100")
# print(url_list)
# print(len(url_list))