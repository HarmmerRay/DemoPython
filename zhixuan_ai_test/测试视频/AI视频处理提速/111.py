from moviepy.editor import VideoFileClip, ImageClip
import numpy as np

def create_gradient_mask(video_height, video_width):
    """
    创建上下方透明渐变的蒙版。
    上方：从中间到底部透明度逐渐增加。
    下方：从中间到顶部透明度逐渐增加。
    """
    # 创建一个全黑的数组，范围 [0, 1]
    mask = np.zeros((video_height, video_width), dtype=np.float32)

    # 渐变部分的高度
    gradient_height = video_height // 4

    # 上方渐变：从中间到底部，透明度逐渐递增
    for y in range(gradient_height):
        # 0 - 1
        alpha = y / gradient_height  # 透明度比例
        mask[y, :] = alpha

    # 下方渐变：从中间到顶部，透明度逐渐递增
    for y in range(gradient_height):
        alpha = y / gradient_height
        mask[video_height - gradient_height + y, :] = alpha

    # 中间保持完全不透明
    mask[gradient_height:video_height - gradient_height, :] = 1

    return mask

def apply_gradient(video_path, output_path):
    # 加载原视频
    clip = VideoFileClip(video_path)
    video_width, video_height = clip.size

    # 创建渐变蒙版
    gradient_mask_array = create_gradient_mask(video_height, video_width)

    # 用 ImageClip 创建 MaskClip
    gradient_mask_clip = ImageClip(gradient_mask_array, ismask=True)
    gradient_mask_clip = gradient_mask_clip.set_duration(clip.duration)

    # 应用渐变蒙版
    result = clip.set_mask(gradient_mask_clip)

    # 输出到文件
    result.write_videofile(output_path, codec="libvpx-vp9", fps=clip.fps)

# 使用示例
video_path = "111.mp4"
output_path = "output.webm"
apply_gradient(video_path, output_path)


这个代码执行出来的视频效果，是视频变得很糊且没有哪一处有渐变的效果