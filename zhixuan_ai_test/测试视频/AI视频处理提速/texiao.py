from moviepy.video.fx.rotate import rotate
from moviepy.video.io.VideoFileClip import VideoFileClip

def rotate_90(video_path="111.mp4"):
    video_clip = VideoFileClip(video_path)
    rotate_clip = rotate(video_clip, 90)
    rotate_clip.write_videofile("111_90.mp4")
    rotate_clip.close()


if __name__ == '__main__':
    rotate_90()
