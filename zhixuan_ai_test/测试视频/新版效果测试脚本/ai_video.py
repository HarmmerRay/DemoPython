import os
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
            "clean_info": 0,
            "up_bottom_cover": 0,
            "change_face": 0,
            "visible_texture": 0,
            "visible_texture_id": 0,
            "visible_texture_pos": "topBottom",
            "invisible_texture": 0,
            "up_short_title": 0,
            "up_comment": 0,
            "ai_audio": 0,
            "yinse_id": 0,
            "cover_caption": 0,
            "add_bgm": 0,
            "add_bgm_id": 0,
            "add_opening": 0,
            "add_opening_id": 0,
            "add_closing": 0,
            "add_closing_id": 0,
            "change_frame_order": 1
        }
    }
url_list = dao.query2("select url from list order by id desc limit 1000")
# # 请求地址
# url2 = "http://127.0.0.1:5000/new_deal"
url2 = "http://49.233.169.177:8080/new_deal"
# 循环发送20个POST请求
num = 0
for url in url_list:
    if num >= 10:
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
        if float(result) > 20.0:
            continue
        num += 1
        data['url'] = str(url['url'])
        print(data)
        response = requests.post(url2, json=data, timeout=3600)  # 设置等待时长为1小时
        print(f"Request {url} sent successfully.")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.json()}\n\n")
        # 将响应内容写入文件，一行一行追加
        with open("all_responses.txt", "a", encoding="utf-8") as file:
            file.write(f"Response content: {json.dumps(response.json(), ensure_ascii=False)}\n")
    except requests.exceptions.RequestException as e:
        print(f"Request {url} failed: {e}")

# https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/d02dd4c7-8799-11ef-93ca-84959735d760.mp4
# https://renyajun-1254809262.cos.ap-beijing.myqcloud.com//daihuo/sucai/d02dd4c7-8799-11ef-93ca-84959735d760.mp4
# url_list = dao.query2("select url from list order by id desc limit 100")
# print(url_list)
# print(len(url_list))