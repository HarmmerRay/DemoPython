# 1. 将.1.jpg图片转为base64数据
# 2. 携带"img_base64"="",发送post请求，到http://49.233.169.177:8080/face_detect_img
# 3. 打印返回得数据

import base64
import os

import requests

def image_to_base64(image_path):
    # 读取图片文件
    with open(image_path, "rb") as image_file:
        # 使用base64模块对图片进行编码
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

def send_post_request(img_base64, url):
    # print(img_base64)
    # 构造POST请求的数据
    payload = {"img_base64": img_base64}
    # 设置请求头为JSON格式
    headers = {'Content-Type': 'application/json'}
    # 发送POST请求
    response = requests.post(url, json=payload, headers=headers,timeout=50)
    # 返回响应
    return response

def main(image_path):
    print("main---",image_path)
    # 转换图片为Base64
    img_base64 = image_to_base64(image_path)
    # 目标URL
    url = 'http://49.233.169.177:8080/face_detect_img'
    # url = 'http://152.136.33.202:8080/face_detect_img'
    # 发送请求并获取响应
    response = send_post_request(img_base64, url)
    # 打印响应数据
    print(response.text)

if __name__ == "__main__":
    folder_path = "./pic"
    for image_path in os.listdir(folder_path):
        if image_path.endswith(('.jpg','.jpeg')):
            image_path = "./pic/" + image_path
            main(image_path)
    # image_path = "./pic/pexels-eberhardgross-443446.jpg"
    # main(image_path)