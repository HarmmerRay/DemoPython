import asyncio
import concurrent
import datetime

import cv2
from concurrent.futures import ThreadPoolExecutor
import torch


# # 加载视频
# cap = cv2.VideoCapture('./test.mp4')
# # 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
# face_detect = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
#
# while True:
#     # 读取视频片段
#     ret, frame = cap.read()
#     if not ret:  # 读完视频后falg返回False
#         break
#     frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
#     # 灰度处理
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
#     face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)
#     # 绘制矩形和圆形检测人脸
#     for x, y, w, h in face_zone:
#         cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
#         cv2.circle(frame, center=(x + w // 2, y + h // 2), radius=w // 2, color=[0, 255, 0], thickness=2)
#     # 显示图片
#     cv2.imshow('video', frame)
#     # 设置退出键和展示频率
#     if ord('q') == cv2.waitKey(40):
#         break
#
# # 释放资源
# cv2.destroyAllWindows()
# cap.release()
# def detect_faceA(video_path, cascade_path, duration_limit_ratio=0.1):
#     print("检测人脸时长占比开始-------")
#     start_time = datetime.datetime.now()
#     # 加载视频
#     cap = cv2.VideoCapture(video_path)
#     # 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
#     face_detect = cv2.CascadeClassifier(cascade_path)
#
#     total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     total_duration = total_frames / fps
#     face_duration = 0.0
#
#     while True:
#         # 读取视频片段
#         ret, frame = cap.read()
#         if not ret:  # 读完视频后flag返回False
#             break
#         frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
#         # 灰度处理
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
#         face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)
#
#         if len(face_zone) > 0:
#             face_duration += 1 / fps
#
#     cap.release()
#     end_time = datetime.datetime.now()
#
#     print("start_time:", start_time, "end_time", end_time, "花费时间:",
#           "{:.1f}".format((end_time - start_time).total_seconds()))
#     print("人脸出现的时长:", round(face_duration, 2), "s,总时长:", round(total_duration, 2), "s,人脸出现的时长占比:",
#           round(face_duration / total_duration, 2) * 100, "%", )
#     # 计算人脸出现的视频片段时长是否不超过视频总时长的10%
#     return face_duration <= (total_duration * duration_limit_ratio)


# 由于第一个逐帧检查比较耗时，这个方法为跳帧检测，跳的越多检测越快相应结果精确度降低
# 添加异步任务，启动子线程执行同时执行多个任务
def detect_faceB(video_path, cascade_path, skip_frames=1):
    start_time = datetime.datetime.now()
    print(f"开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    cap = cv2.VideoCapture(video_path)
    face_detect = cv2.CascadeClassifier(cascade_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    detected_frames = 0
    face_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if detected_frames % (skip_frames + 1) == 0:
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

            if len(face_zone) > 0:
                face_frames += 1

        detected_frames += 1

    cap.release()

    face_percentage = (face_frames / (detected_frames / (skip_frames + 1))) * 100
    end_time = datetime.datetime.now()
    print(f"结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    print(f"包含人脸的帧数与检测到的帧数的百分比： {round(face_percentage, 2)}% - 视频: {video_path}")
    print(f"检测耗时: {round((end_time - start_time).total_seconds(), 2)} - 视频: {video_path}")
    return face_percentage


# async def mainB():
#     video_paths = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4",
#                    "video6.mp4", "video7.mp4", "video8.mp4", "video9.mp4", "video10.mp4"]
#     cascade_path = "haarcascade_frontalface_default.xml"
#     tasks = [detect_faceB(video_path, cascade_path) for video_path in video_paths]
#     results = await asyncio.gather(*tasks)
#     for video_path, result in zip(video_paths, results):
#         print(f"视频: {video_path} - 人脸百分比: {round(result, 2)}%")

# 提升单个视频处理的效率
def process_frame(frame, face_detect):
    # 缩小到原来大小一半
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 每次图像尺寸缩小20%  候选矩形框检测超过3次则有效
    face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
    # [x,y,w,h]的矩形块坐标表示
    return len(face_zone) > 0


# 跳大帧，高缩放，少候选 如果超出则false,不超则true
def detect_faceC(video_path, cascade_path, skip_frames=2):
    start_time = datetime.datetime.now()
    print(f"开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    cap = cv2.VideoCapture(video_path)
    face_detect = cv2.CascadeClassifier(cascade_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    detected_frames = 0
    face_frames = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if detected_frames % (skip_frames + 1) == 0:
                future = executor.submit(process_frame, frame, face_detect)
                if future.result():
                    face_frames += 1

            detected_frames += 1

    cap.release()

    face_percentage = (face_frames / (detected_frames / (skip_frames + 1))) * 100
    end_time = datetime.datetime.now()
    print(f"结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    print(f"包含人脸的帧数与检测到的帧数的百分比： {round(face_percentage, 2)}% - 视频: {video_path}")
    print(f"检测耗时: {round((end_time - start_time).total_seconds(), 2)} - 视频: {video_path}")
    return face_percentage


# 提升同时处理多个视频的效率
# 使用线程池进一步优化，因为检测人脸此任务是 典型的视频处理IO密集型任务，线程池再好不过。
def detect_face_sync(video_path, cascade_path, skip_frames=1):
    start_time = datetime.datetime.now()
    print(f"开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    cap = cv2.VideoCapture(video_path)
    face_detect = cv2.CascadeClassifier(cascade_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    detected_frames = 0
    face_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if detected_frames % (skip_frames + 1) == 0:
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

            if len(face_zone) > 0:
                face_frames += 1

        detected_frames += 1

    cap.release()

    face_percentage = (face_frames / (detected_frames / (skip_frames + 1))) * 100
    end_time = datetime.datetime.now()
    print(f"结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    print(f"包含人脸的帧数与检测到的帧数的百分比： {round(face_percentage, 2)}% - 视频: {video_path}")
    print(f"检测耗时: {round((end_time - start_time).total_seconds(), 2)} - 视频: {video_path}")
    return face_percentage


async def detect_face_async(video_path, cascade_path, skip_frames=1, executor=None):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, detect_face_sync, video_path, cascade_path, skip_frames)


async def mainC():
    video_paths = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4",
                   "video6.mp4", "video7.mp4", "video8.mp4", "video9.mp4", "video10.mp4"]
    cascade_path = "../../zhixuan_ai/ai_test/ai_video/models/haarcascade_frontalface_default.xml"
    with ThreadPoolExecutor(max_workers=10) as executor:
        tasks = [detect_face_async(video_path, cascade_path, executor=executor) for video_path in video_paths]
        results = await asyncio.gather(*tasks)
        for video_path, result in zip(video_paths, results):
            print(f"视频: {video_path} - 人脸百分比: {round(result, 2)}%")


# 使用yolov5检测
def detect_face_yolov5(video_path):
    start_time = datetime.datetime.now()
    print(f"开始时间: {start_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")

    # 加载YOLOv5模型
    model = torch.hub.load('ultralytics/yolov5', 'yolov5n')
    model.eval()

    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    detected_frames = 0
    face_frames = 0

    # 计算skip_frames
    skip_frames = max(1, total_frames // 10)
    times = 1
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if detected_frames % (skip_frames + 1) == 0:
            print("检测的第", times, "帧")
            times += 1
            # 将图像转换为RGB格式
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 进行推理
            results = model(frame_rgb)

            # 解析结果
            for result in results.xyxy[0]:
                x1, y1, x2, y2, conf, cls = result.tolist()
                if cls == 0 and conf > 0.3:  # 假设类别0是人脸
                    face_frames += 1
                    break  # 只统计是否检测到人脸，不绘制框

        detected_frames += 1

    cap.release()

    face_percentage = (face_frames / (detected_frames / (skip_frames + 1))) * 100
    end_time = datetime.datetime.now()
    print(f"结束时间: {end_time.strftime('%Y-%m-%d %H:%M:%S')} - 视频: {video_path}")
    print(f"包含人脸的帧数与检测到的帧数的百分比： {round(face_percentage, 2)}% - 视频: {video_path}")
    print(f"检测耗时: {round((end_time - start_time).total_seconds(), 2)} - 视频: {video_path}")
    return face_percentage

def process_videos(video_paths):
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(detect_face_yolov5, video_path) for video_path in video_paths]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results


video_pathA = './test.mp4'
video_pathB = "./test2_65s.mp4"
cascade_path = '../../zhixuan_ai/ai_test/ai_video/models/haarcascade_frontalface_default.xml'
# print("Detect_faceB 21s原视频…………………………")
# detect_faceB(video_pathA, cascade_path, 1)
# print("Detect_faceC 21s原视频…………………………")
# detect_faceC(video_pathA, cascade_path)
print("Detect_face_yolov5 21s原视频…………………………")
detect_face_yolov5(video_pathA)
# print("Detect_faceA 65s原视频…………………………")
# detect_faceA(video_pathB,cascade_path)
# print("Detect_faceB 65s原视频…………………………")
# detect_faceB(video_pathB, cascade_path, 2)
