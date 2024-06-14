import os
import subprocess
from PIL import Image


# @author: Hammer
# 顺次将文件夹里的所有.webm文件用ffmpeg在00:00:01处提取一帧.jpg文件
def extract_frames_from_webm(directory):
    if not os.path.isdir(directory):
        print(f"Error: Directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        if filename.endswith('.webm'):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{os.path.splitext(filename)[0]}.jpg")

            command = [
                'ffmpeg',
                '-i', input_path,
                '-vframes', '1',
                '-ss', '00:00:01',
                output_path
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Successfully extracted frame from {filename}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to extract frame from {filename}: {e}")


# @author: Hammer
#
def resize_jpg_images(input_dir, output_dir, width=320, height=320):
    # 创建输出目录，如果它还不存在的话
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历输入目录中的所有.jpg文件
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.jpg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # 使用ffmpeg调整图片大小
            command = [
                'ffmpeg',
                '-i', input_path,
                '-vf', f'scale={width}:{height}',
                '-qscale:v', '2',  # 质量控制，数值越小质量越高，但文件越大
                output_path
            ]

            try:
                subprocess.run(command, check=True)
                print(f"Resized and saved {filename} to {output_dir}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to resize {filename}: {e}")


def resize_image(input_image_path, output_image_path, size=(320, 320)):
    original_image = Image.open(input_image_path)
    resized_image = original_image.resize(size, Image.Resampling.BICUBIC)
    resized_image.save(output_image_path)


def batch_resize_images(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            resize_image(input_path, output_path)


input_directory = 'D:\Desktop\ccc'
output_directory = 'D:\Desktop\caa'
batch_resize_images(input_directory, output_directory)

# resize_jpg_images(input_directory, output_directory)

# extract_frames_from_webm('D:\Desktop\webm')
