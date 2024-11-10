import random
import subprocess

from moviepy.video.io.VideoFileClip import VideoFileClip


def special_effect_add(video_path, option):
    output_path = video_path + ".texiao.avi"
    if option == 1:
        print("视频开始加速")
        speed_factor = random.uniform(1.05, 1.1)
        print("speed_factor:", speed_factor)
        dao_speed_factor = 1 / speed_factor
        acceleration_cmd = f"""ffmpeg -i {video_path} -vf "setpts={dao_speed_factor}*PTS" -af "atempo={dao_speed_factor}" -map_metadata -1 -c:v rawvideo -c:a aac -y {output_path} """
        print(acceleration_cmd)
        subprocess.run(acceleration_cmd, shell=True)
        print("视频加速完成")
    if option == 2:
        print("视频开始放大")
        bigger_factor = random.uniform(0.95, 0.9)
        width,height = VideoFileClip(video_path).size
        print(width,',',height)
        # 计算裁剪区域
        crop_width = width * bigger_factor
        crop_height = height * bigger_factor
        left = width - crop_width / 2
        top = height - crop_height / 2
        print("bigger_factor", bigger_factor)
        bigger_cmd = f"""ffmpeg -i {video_path} -vf "crop={crop_width}:{crop_height}:{left}:{top},scale={width}:{height}" -map_metadata -1 -pix_fmt yuv420p -c:v rawvideo -c:a aac -y {output_path}"""
        print(bigger_cmd)
        subprocess.run(bigger_cmd, shell=True)
        print("视频放大完成")
    if option == 3:
        print("视频开始缩小")
        smaller_factor = random.uniform(0.95, 0.9)
        print("smaller_factor", smaller_factor)
        width, height = VideoFileClip(video_path).size
        print(width, ',', height)
        smaller_cmd = f"""ffmpeg -i {video_path} -vf "scale=iw*{smaller_factor}:-1,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black" -map_metadata -1 -pix_fmt yuv420p -c:v rawvideo -c:a aac -y {output_path} """
        print(smaller_cmd)
        subprocess.run(smaller_cmd, shell=True)
        print("视频缩小完成")
    if option == 4:
        print("视频开始增加颜色饱和度")
        saturation_factor = random.uniform(1.05, 1.2)
        print("saturation_factor", saturation_factor)
        saturation_cmd = f"""ffmpeg -i {video_path} -vf "eq=saturation={saturation_factor}" -map_metadata -1 -pix_fmt yuv420p -c:v rawvideo -c:a aac -y {output_path}"""
        print(saturation_cmd)
        subprocess.run(saturation_cmd, shell=True)
        print("视频颜色增加饱和度完成")
    if option == 5:
        print("视频开始增加锐化效果")
        sharpness_factor = random.uniform(1.1, 1.3)
        print("sharpness_factor", sharpness_factor)
        sharpen_cmd = f"""ffmpeg -i {video_path} -vf "unsharp=5:5:{sharpness_factor}:5:5:0.0" -map_metadata -1 -pix_fmt yuv420p -c:v rawvideo -c:a aac -y {output_path}"""
        print(sharpen_cmd)
        subprocess.run(sharpen_cmd, shell=True)
        print("视频增加锐化效果完成")
    return output_path

special_effect_add('2.mp4',3)