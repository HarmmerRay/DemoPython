import datetime

import cv2


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
def is_face_duration_within_limit(video_path, cascade_path, duration_limit_ratio=0.1):
    print("检测人脸时长占比开始-------")
    start_time = datetime.datetime.now()
    # 加载视频
    cap = cv2.VideoCapture(video_path)
    # 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
    face_detect = cv2.CascadeClassifier(cascade_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_duration = total_frames / fps
    face_duration = 0.0

    while True:
        # 读取视频片段
        ret, frame = cap.read()
        if not ret:  # 读完视频后flag返回False
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        # 灰度处理
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
        face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

        if len(face_zone) > 0:
            face_duration += 1 / fps

    cap.release()
    end_time = datetime.datetime.now()

    print("start_time:", start_time, "end_time", end_time, "花费时间:", "{:.1f}".format((end_time - start_time).total_seconds()))
    print("人脸出现的时长:", round(face_duration, 2), "s,总时长:", round(total_duration, 2), "s,人脸出现的时长占比:",
          round(face_duration / total_duration, 2) * 100, "%", )
    # 计算人脸出现的视频片段时长是否不超过视频总时长的10%
    return face_duration <= (total_duration * duration_limit_ratio)


video_path = './test.mp4'
cascade_path = './haarcascade_frontalface_default.xml'
result = is_face_duration_within_limit(video_path, cascade_path)
print(result)


def detect_faces(video_path, cascade_path, skip_frames=1):
    # 加载视频
    cap = cv2.VideoCapture(video_path)
    # 创建一个级联分类器 加载一个.xml分类器文件 它既可以是Haar特征也可以是LBP特征的分类器
    face_detect = cv2.CascadeClassifier(cascade_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    detected_frames = 0
    face_frames = 0

    while True:
        ret, frame = cap.read()
        if not ret:  # 读完视频后flag返回False
            break

        # 跳帧检测
        if detected_frames % (skip_frames + 1) == 0:
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
            # 灰度处理
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 多个尺度空间进行人脸检测   返回检测到的人脸区域坐标信息
            face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

            if len(face_zone) > 0:
                face_frames += 1

        detected_frames += 1

    cap.release()

    # 计算包含人脸的帧数与检测到的帧数的百分比
    face_percentage = (face_frames / (detected_frames / (skip_frames + 1))) * 100
    return face_percentage