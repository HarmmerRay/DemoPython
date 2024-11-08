import subprocess

from moviepy.video.io.VideoFileClip import VideoFileClip


# Step 1: Generate PNG image using ImageMagick
def generate_image():
    size_position_list = [{"size": "400x250", "geometry1": "+0+0", "geometry2": "+0+60", "geometry3": "+0+125",
                           "yellow_box_size": "400x67", "font_size1": "40", "font_size2": "45", "font_size3": "33",
                           "strokewidth": "2"},
                          {"size": "1280x720", "geometry1": "+0+0", "geometry2": "+0+210", "geometry3": "+0+430",
                           # "yellow_box_size": "1280x200", "font_size1": "130", "font_size2": "140", "font_size3": "106",
                           "yellow_box_size": "1280x200", "font_size1": "135", "font_size2": "140", "font_size3": "128",
                           "strokewidth": "6"},
                          {"size": "2048x1080", "geometry1": "+0+0", "geometry2": "+0+240", "geometry3": "+0+500",
                           "yellow_box_size": "1600x268", "font_size1": "160", "font_size2": "180",
                           "font_size3": "150", "strokewidth": "0"},
                          {"size": "4096x2160", "geometry1": "+0+0", "geometry2": "+0+450", "geometry3": "+0+960",
                           "yellow_box_size": "3296x470","red_box_size": "4096x390", "font_size1": "300", "font_size2": "320",
                           "font_size3": "260", "strokewidth": "40"},
                          ]
    size_position = size_position_list[3]
    command = [
        'magick',
        '-size', size_position['size'], 'xc:none',
        # 生成描边图层
        '(',
        '-background', 'transparent',
        '-fill', 'none',  # 不填充任何颜色
        '-stroke', 'black',
        '-strokewidth', size_position['strokewidth'],
        '-pointsize', size_position['font_size1'],
        '-font', './SourceHanSansSC-Bold-2.otf',
        '-gravity', 'north',
        'label:智选AI带货系统',  # 仅作为描边的轮廓
        ')',
        '-geometry', size_position['geometry1'],
        '-composite',

        # 生成文字图层
        '(',
        '-background', 'transparent',
        '-fill', '#E2CA09',  # 设置文字颜色
        '-stroke', 'none',  # 不设置描边
        '-pointsize', size_position['font_size1'],
        '-font', './SourceHanSansSC-Bold-2.otf',
        '-gravity', 'north',
        'label:智选AI带货系统',
        ')',
        '-geometry', size_position['geometry1'],
        '-composite',

        # 第二行黄色背景矩形
        '(',
        '-size', size_position['yellow_box_size'],  # 仅覆盖第二行的区域
        'xc:#F0CC04',#F0CC04  #EED204
        ')',
        '-geometry', size_position['geometry2'],
        '-composite',
        '(',
        '-background', 'transparent',
        '-fill', '#000000',
        '-pointsize', size_position['font_size2'],
        '-font', './SourceHanSansSC-Bold-2.otf',
        '-gravity', 'north',
        'label:智选AI带货系统统统统',
        ')',
        '-geometry', size_position['geometry2'],
        '-composite',

        # 第三行黄色背景矩形
        '(',
        '-size', size_position['red_box_size'],  # 仅覆盖第二行的区域
        'xc:#B81C1D',  # F0CC04  #EED204
        ')',
        '-geometry', size_position['geometry3'],
        '-composite',
        # 第三行文字
        '(',
        '-background', 'transparent',
        '-fill', 'white',
        '-stroke', 'none',
        '-pointsize', size_position['font_size3'],
        '-font', './SourceHanSansSC-Bold-2.otf',
        '-gravity', 'north',
        'label:网友：智选AI带货系统',
        ')',
        '-geometry', size_position['geometry3'],
        '-composite',

        'output_text.png'
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error generating image: {result.stderr}")
    else:
        print("Image generated successfully")


# Step 2: Overlay image on video using FFmpeg
def overlay_image_on_video(video_input, image_input, video_output):
    video_clip = VideoFileClip(video_input)
    width,height = video_clip.size
    print(width,height)

    command = [
        'ffmpeg',
        '-i', video_input,
        '-i', image_input,
        '-filter_complex',
        f'[1:v]scale={width}:-1[logo]; [0:v][logo]overlay=(W-w)/2:H*0.07',
        '-c:a', 'copy', '-y',
        video_output
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error overlaying image on video: {result.stderr}")
    else:
        print("Video with overlay generated successfully")


# Main function to run the steps
def main():
    # Paths to input and output files
    video_input = '1.mp4'
    image_input = 'output_text.png'
    video_output = 'output_video.mp4'

    # Generate the image
    generate_image()

    # Overlay the image on the video
    overlay_image_on_video(video_input, image_input, video_output)


if __name__ == '__main__':
    main()
