# -*- coding:utf-8 -*-
import os
import re
import time

import requests

import random

from xBogus import XBogus


def get_cookie_str(cookies):
    cookie_str = ""
    for cookie in cookies:
        cookie_str += f"{cookie['name']}={cookie['value']};"
    # 移除最后一个分号
    cookie_str = cookie_str.rstrip(";")
    return cookie_str


def analyze_user_input(user_in, session, headers):
    try:
        u = re.search('user/([-\w]+)', user_in)
        if u:
            return u.group(1)
        u = re.search('https://v.douyin.com/(\w+)/', user_in)
        if u:
            url = u.group(0)
            res = session.get(url=url, headers=headers).url
            uid = re.search('user/([-\w]+)', res)
            if uid:
                return uid.group(1)

    except Exception as e:
        return


def generate_url_with_xbs(url, user_agent):
    query = urllib.parse.urlparse(url).query
    xbogus = execjs.compile(open('X-Bogus.js').read()).call('sign', query, user_agent)
    return xbogus


# 默认开启睡眠
def get_home_video(user_in, cookies, sleep=True, limit=200):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'Referer': 'https://www.douyin.com/',
        'Cookie': get_cookie_str(cookies)
    }
    session = requests.Session()
    # 防止开vpn了requests模块报ssl异常
    session.trust_env = False

    author_name = ''
    sec_uid = analyze_user_input(user_in, session, headers)
    cursor = 0
    if sec_uid is None:
        return None
    # home_url = f'https://www.douyin.com/aweme/v1/web/aweme/post/?aid=6383&sec_user_id={sec_uid}&count=1&max_cursor={cursor}&cookie_enabled=true&platform=PC&downlink=10'

    # xbs = XBogusUtil.generate_url_with_xbs(home_url, headers.get('User-Agent'))

    # url = home_url + '&X-Bogus=' + xbs
    # json_str = session.get(url, headers=headers).json()

    # author_name = json_str['aweme_list'][0]['author']['nickname']  # 获取作者名称
    video_list = []
    while 1:
        print("start get home video", cursor, sec_uid)
        home_url = f'https://www.douyin.com/aweme/v1/web/aweme/post/?aid=6383&sec_user_id={sec_uid}&count=18&max_cursor={cursor}&cookie_enabled=true&platform=PC&downlink=10'
        xbs = generate_url_with_xbs(home_url, headers.get('User-Agent'))
        url = home_url + '&X-Bogus=' + xbs
        json_str = session.get(url, headers=headers)
        # print("get video info:",json_str.text)
        if not json_str.text:
            return video_list
        json_str = json_str.json()

        if "max_cursor" not in json_str:
            break

        cursor = json_str["max_cursor"]  # 当页页码
        print("cursor", cursor)
        for i1 in json_str["aweme_list"]:
            #  视频收集
            if i1["images"] is None:
                # name = i1["desc"]
                # url = i1["video"]["play_addr"]["url_list"][0]
                video_list.append(i1)
                # url = i1["video"]['bit_rate'][0]['play_addr']['url_list'][0]
                # self.video_info_list.append({'video_desc': name, 'video_url': url})
            #  图片收集
            else:
                # self.picture_info_list += list(map(lambda x: x["url_list"][-1], i1["images"]))
                pass
        if json_str["has_more"] == 0 or len(video_list) > limit:
            break

        # 随机睡眠

        time.sleep(random.randint(5, 10) / 10)
        print("current page", cursor)

        # break
    return video_list


def search_douyin(keyword, count=10):
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "search_channel": 'aweme_video_web',
        "sort_type": 0,
        "publish_time": 0,
        "keyword": keyword,
        "search_source": "tab_search",
        "query_correct_type": "1",
        "is_filter_search": 0,
        "from_group_id": "",
        "offset": 0,
        "count": count,
        "pc_client_type": "1",
        "version_code": "170400",
        "version_name": "17.4.0",
        "cookie_enabled": "true",
        "platform": "PC",
        "downlink": "10",
    }
    print("调用craw.py的search_douyin")
    # self.__add_ms_token(params)
    # self.deal_url_params(params, 4 if self.cursor else 8)
    xb = XBogus()
    params["X-Bogus"] = xb.get_x_bogus(params, 8)
    headers = {
        "Referer": "https://www.douyin.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
    }
    response = requests.get("https://www.douyin.com/aweme/v1/web/search/item/", params, headers=headers)
    #
    return response.json()


def get_video_list(daren_url):
    video_list = search_douyin(daren_url, count=1)
    print("视频列表", video_list)
    if not video_list or 'data' not in video_list:
        print("没有视频")
    videos = []
    for v in video_list['data']:
        if 'data_size' in v['aweme_info']['video']['play_addr']:
            size = v['aweme_info']['video']['play_addr']['data_size'] / 1024 / 1024
        else:
            size = 0
        videos.append({
            "video_id": v['aweme_info']['aweme_id'],
            "name": v['aweme_info']['desc'],
            "url": v['aweme_info']['video']['play_addr']['url_list'][0],
            'pic': v['aweme_info']['video']['cover']['url_list'][0],
            'size': size,

        })
        return video_list


if __name__ == "__main__":
    video_list = get_video_list("https://www.douyin.com/user/MS4wLjABAAAAB92s1iYJ6Kr4B6RpP3zenR2DywmkuBBX-RKYLExuNHk")
    print(video_list)
