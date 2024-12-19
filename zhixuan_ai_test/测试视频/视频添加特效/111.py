import random

from moviepy.video.io.VideoFileClip import VideoFileClip


def plusglshade(video_path):
    video_out = video_path + ".texiao.mp4"
    names = ['split_4_','star_','mirror_','sway_','jitter_','preview_','soul_',
               'split_interval_','stab_ci_','test_','white_mask_','split_9_','split_vert2_']
    video_clip = VideoFileClip(video_path)
    width, height = video_clip.size
    duration = video_clip.duration
    # 480s
    start_times = []
    start = 0
    head_cmd = f"""xvfb-run -a --server-args="-screen 0 {width}x{height}x24 -nolisten tcp -dpi 96 +extension RANDR" /home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i {video_path} -filter_complex " """
    num = 0
    while start < duration:

        start += round(random.uniform(5, 10), 2)
        start_times.append(start)
        name = random.choice(names)
        if num == 0 :
            head_cmd += f"""[{num}:v]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:duration=5[{num}v] """
        else:
            head_cmd += f"""[{num-1}v]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:duration=5[{num}v] """
    tail_cmd = f"""-map "{num-1}v" -c:v libx264 -c:a aac -pix_fmt yuv420p -y {video_out} """
    head_cmd += tail_cmd
    print(head_cmd)
    print(start_times)
plusglshade()
# names = ['split_4_', 'star_', 'mirror_', 'sway_', 'jitter_', 'preview_', 'soul_',
#          'split_interval_', 'stab_ci_', 'test_', 'white_mask_', 'split_9_', 'split_vert2_']
#
# name = random.choice(names)
# print(name)