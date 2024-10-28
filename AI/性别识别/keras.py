import tensorflow as tf

import face_recognition
import cv2
import numpy as np

def load_gender_model(model_path):
    return tf.keras.models.load_model(model_path)


def detect_face(image_path):
    # 加载你的图片
    image = face_recognition.load_image_file(image_path)

    # 找到图像中所有人脸的位置
    face_locations = face_recognition.face_locations(image)

    print("在这张图片中找到了 {} 张脸。".format(len(face_locations)))

    return face_locations, image


def predict_gender(image_path, model):
    face_locations, image = detect_face(image_path)

    for face_location in face_locations:
        # 获取人脸的位置信息
        top, right, bottom, left = face_location

        # 裁剪人脸区域
        face_image = image[top:bottom, left:right]

        # 将图像转换为灰度图像（如果模型需要）
        face_image_gray = cv2.cvtColor(face_image, cv2.COLOR_RGB2GRAY)

        # 调整图像大小以匹配模型输入
        face_image_resized = cv2.resize(face_image_gray, (100, 100))

        # 归一化图像数据
        face_image_normalized = face_image_resized.astype('float32') / 255.0

        # 增加维度以匹配模型输入
        face_image_expanded = np.expand_dims(face_image_normalized, axis=[0, -1])

        # 使用模型进行预测
        prediction = model.predict(face_image_expanded)
        gender = 'Male' if prediction[0][0] > 0.5 else 'Female'

        # 在原图上标注性别
        cv2.rectangle(image, (left, top), (right, bottom), (255, 0, 0), 2)
        cv2.putText(image, gender, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # 显示结果图像
    cv2.imshow('Gender Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 示例用法
model_path = './model_1.keras'  # 替换为你的模型路径
model = load_gender_model(model_path)

image_path = '11.jpg'  # 替换为你想要测试的图片路径
predict_gender(image_path, model)
