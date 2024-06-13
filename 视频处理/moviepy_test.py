from moviepy.editor import *


def split_video(input_file, start_time, end_time, output_file):
    video = input_file
    subclip = video.subclip(start_time, end_time)
    subclip.write_videofile(output_file)
    video.close()


if __name__ == '__main__':
    input_file = VideoFileClip('demo.mp4')
    output_file = 'output.mp4'
    duration = input_file.duration
    start_time = duration / 10
    end_time = duration / 5
    split_video(input_file, start_time, end_time, output_file)
