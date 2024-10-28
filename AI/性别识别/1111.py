# Use a pipeline as a high-level helper
import face_recognition
from transformers import pipeline

def detect_face(image_path):

    # 加载你的图片
    image = face_recognition.load_image_file(image_path)

    # 找到图像中所有人脸的位置
    face_locations = face_recognition.face_locations(image)

    print("在这张图片中找到了 {} 张脸。".format(len(face_locations)))

    # 在图片上绘制人脸边框
    for face_location in face_locations:
        # 打印每张脸的位置信息
        top, right, bottom, left = face_location
        print("人脸位于 顶部: {}, 右侧: {}, 底部: {}, 左侧: {}".format(top, right, bottom, left))
    return face_locations

pipe = pipeline("image-classification", model="rizvandwiki/gender-classification")

# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("rizvandwiki/gender-classification")
model = AutoModelForImageClassification.from_pretrained("rizvandwiki/gender-classification")