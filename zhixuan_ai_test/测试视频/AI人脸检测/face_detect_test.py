import os
import subprocess
import traceback
import json
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

from moviepy.video.io.VideoFileClip import VideoFileClip
from zhixuan_ai_test.db import dao

url_list = dao.query2("select url from list order by id desc limit 10")
# url_list = [{
#     "url": "https://v26-default.ixigua.com/0fa9c58b6b127a136f4aa0a480b47c29/6713369d/video/tos/cn/tos-cn-ve-15/oAA8iACf2zSfA3MbWXne8X3VBtbDLQeAIlMPEC/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=1418&cs=0&ds=3&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZmNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=Njk2PDo4Zzk4Zjw3ODRmNkBpM2Q8ZnU5cjw5dTMzNGkzM0BeNjQtLV8zNjMxNS9hLTJfYSNwNmlhMmRjX3NgLS1kLS9zcw%3D%3D&btag=80000e00020000&dy_q=1729308769&feature_id=aa7df520beeae8e397df15f38df0454c&l=202410191132497307F7C81B2E3D808910"},
#     {
#         "url": "https://v3-default.ixigua.com/89ed42f61f303847f84b8134fca37ac2/67133662/video/tos/cn/tos-cn-ve-15/os6AGflFQge9D3SIgWiEAPBDzAAFQnzLnVIghA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1794&bt=1794&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApVHNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGdpZTYzZGc7Zzs2NTM8aUBpamRmNGs5cjY4djMzNGkzM0AuMWJgNi4uNWMxYF9iNWFeYSNlZGE1MmRzMS5gLS1kLTBzcw%3D%3D&btag=80000e00018000&dy_q=1729308712&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20241019113152A62A4ADEB3A5257FC4A5"},
#     {
#         "url": "https://v26-default.ixigua.com/0fa9c58b6b127a136f4aa0a480b47c29/6713369d/video/tos/cn/tos-cn-ve-15/oAA8iACf2zSfA3MbWXne8X3VBtbDLQeAIlMPEC/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=1418&cs=0&ds=3&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZmNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=Njk2PDo4Zzk4Zjw3ODRmNkBpM2Q8ZnU5cjw5dTMzNGkzM0BeNjQtLV8zNjMxNS9hLTJfYSNwNmlhMmRjX3NgLS1kLS9zcw%3D%3D&btag=80000e00020000&dy_q=1729308769&feature_id=aa7df520beeae8e397df15f38df0454c&l=202410191132497307F7C81B2E3D808910"},
#     {
#         "url": "https://v3-default.ixigua.com/89ed42f61f303847f84b8134fca37ac2/67133662/video/tos/cn/tos-cn-ve-15/os6AGflFQge9D3SIgWiEAPBDzAAFQnzLnVIghA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1794&bt=1794&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApVHNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGdpZTYzZGc7Zzs2NTM8aUBpamRmNGs5cjY4djMzNGkzM0AuMWJgNi4uNWMxYF9iNWFeYSNlZGE1MmRzMS5gLS1kLTBzcw%3D%3D&btag=80000e00018000&dy_q=1729308712&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20241019113152A62A4ADEB3A5257FC4A5"}
#     , {
#         "url": "https://v26-default.ixigua.com/0fa9c58b6b127a136f4aa0a480b47c29/6713369d/video/tos/cn/tos-cn-ve-15/oAA8iACf2zSfA3MbWXne8X3VBtbDLQeAIlMPEC/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=1418&cs=0&ds=3&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZmNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=Njk2PDo4Zzk4Zjw3ODRmNkBpM2Q8ZnU5cjw5dTMzNGkzM0BeNjQtLV8zNjMxNS9hLTJfYSNwNmlhMmRjX3NgLS1kLS9zcw%3D%3D&btag=80000e00020000&dy_q=1729308769&feature_id=aa7df520beeae8e397df15f38df0454c&l=202410191132497307F7C81B2E3D808910"},
#     {
#         "url": "https://v3-default.ixigua.com/89ed42f61f303847f84b8134fca37ac2/67133662/video/tos/cn/tos-cn-ve-15/os6AGflFQge9D3SIgWiEAPBDzAAFQnzLnVIghA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1794&bt=1794&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApVHNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGdpZTYzZGc7Zzs2NTM8aUBpamRmNGs5cjY4djMzNGkzM0AuMWJgNi4uNWMxYF9iNWFeYSNlZGE1MmRzMS5gLS1kLTBzcw%3D%3D&btag=80000e00018000&dy_q=1729308712&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20241019113152A62A4ADEB3A5257FC4A5"},
#     {
#         "url": "https://v26-default.ixigua.com/0fa9c58b6b127a136f4aa0a480b47c29/6713369d/video/tos/cn/tos-cn-ve-15/oAA8iACf2zSfA3MbWXne8X3VBtbDLQeAIlMPEC/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=1418&cs=0&ds=3&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZmNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=Njk2PDo4Zzk4Zjw3ODRmNkBpM2Q8ZnU5cjw5dTMzNGkzM0BeNjQtLV8zNjMxNS9hLTJfYSNwNmlhMmRjX3NgLS1kLS9zcw%3D%3D&btag=80000e00020000&dy_q=1729308769&feature_id=aa7df520beeae8e397df15f38df0454c&l=202410191132497307F7C81B2E3D808910"},
#     {
#         "url": "https://v3-default.ixigua.com/89ed42f61f303847f84b8134fca37ac2/67133662/video/tos/cn/tos-cn-ve-15/os6AGflFQge9D3SIgWiEAPBDzAAFQnzLnVIghA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1794&bt=1794&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApVHNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGdpZTYzZGc7Zzs2NTM8aUBpamRmNGs5cjY4djMzNGkzM0AuMWJgNi4uNWMxYF9iNWFeYSNlZGE1MmRzMS5gLS1kLTBzcw%3D%3D&btag=80000e00018000&dy_q=1729308712&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20241019113152A62A4ADEB3A5257FC4A5"},
#     {
#         "url": "https://v26-default.ixigua.com/0fa9c58b6b127a136f4aa0a480b47c29/6713369d/video/tos/cn/tos-cn-ve-15/oAA8iACf2zSfA3MbWXne8X3VBtbDLQeAIlMPEC/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=1418&cs=0&ds=3&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZmNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=Njk2PDo4Zzk4Zjw3ODRmNkBpM2Q8ZnU5cjw5dTMzNGkzM0BeNjQtLV8zNjMxNS9hLTJfYSNwNmlhMmRjX3NgLS1kLS9zcw%3D%3D&btag=80000e00020000&dy_q=1729308769&feature_id=aa7df520beeae8e397df15f38df0454c&l=202410191132497307F7C81B2E3D808910"},
#     {
#         "url": "https://v3-default.ixigua.com/89ed42f61f303847f84b8134fca37ac2/67133662/video/tos/cn/tos-cn-ve-15/os6AGflFQge9D3SIgWiEAPBDzAAFQnzLnVIghA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1794&bt=1794&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApVHNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGdpZTYzZGc7Zzs2NTM8aUBpamRmNGs5cjY4djMzNGkzM0AuMWJgNi4uNWMxYF9iNWFeYSNlZGE1MmRzMS5gLS1kLTBzcw%3D%3D&btag=80000e00018000&dy_q=1729308712&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20241019113152A62A4ADEB3A5257FC4A5"},
#     {
#         "url": "https://v26-default.ixigua.com/0fa9c58b6b127a136f4aa0a480b47c29/6713369d/video/tos/cn/tos-cn-ve-15/oAA8iACf2zSfA3MbWXne8X3VBtbDLQeAIlMPEC/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=1418&cs=0&ds=3&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZmNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=Njk2PDo4Zzk4Zjw3ODRmNkBpM2Q8ZnU5cjw5dTMzNGkzM0BeNjQtLV8zNjMxNS9hLTJfYSNwNmlhMmRjX3NgLS1kLS9zcw%3D%3D&btag=80000e00020000&dy_q=1729308769&feature_id=aa7df520beeae8e397df15f38df0454c&l=202410191132497307F7C81B2E3D808910"},
#     {
#         "url": "https://v3-default.ixigua.com/89ed42f61f303847f84b8134fca37ac2/67133662/video/tos/cn/tos-cn-ve-15/os6AGflFQge9D3SIgWiEAPBDzAAFQnzLnVIghA/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1794&bt=1794&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApVHNzZvrKttUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGdpZTYzZGc7Zzs2NTM8aUBpamRmNGs5cjY4djMzNGkzM0AuMWJgNi4uNWMxYF9iNWFeYSNlZGE1MmRzMS5gLS1kLTBzcw%3D%3D&btag=80000e00018000&dy_q=1729308712&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20241019113152A62A4ADEB3A5257FC4A5"}]
url2 = "http://49.233.169.177:8080/face_detect"


def process_url(url):
    # try:
    #     VideoFileClip(url['url'])
    # except Exception as e:
    #     print(url['url'] + "不是视频")
    #     return

    try:
        # cmd = f"ffprobe -v error -select_streams v:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 -i {url['url']}"
        # result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode('utf-8').strip()
        # print("Video duration:", result)
        print(url['url'])
        response = requests.get(url2, params={'url': url['url'], 'count': 8}, timeout=60)
        print(f"Request {url} sent successfully.")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.json()}\n\n")

        # 将响应内容写入文件，一行一行追加
        with open("all_responses2.txt", "a", encoding="utf-8") as file:
            file.write(f"Response content: {json.dumps(response.json(), ensure_ascii=False)}\n")
    except requests.exceptions.RequestException as e:
        print(f"Request {url} failed: {e}")


# 使用线程池并发发送请求
with ThreadPoolExecutor(max_workers=1) as executor:
    futures = []
    num = 0
    for url in url_list:
        if num >= 8:
            break
        futures.append(executor.submit(process_url, url))
        num += 1

    # 等待所有任务完成
    for future in as_completed(futures):
        try:
            future.result()  # 获取任务结果或处理异常
        except Exception as e:
            print(f"An error occurred: {e}")
