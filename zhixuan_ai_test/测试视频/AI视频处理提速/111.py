import datetime
import random
import subprocess

from moviepy.video.io.VideoFileClip import VideoFileClip


def gltransition(video_path):
    begin_time = datetime.datetime.now()
    video_out = video_path + ".trans.mp4"
    transitions = ['crosswarp','wipeleft']
    transition = "/home/ubuntu/ai_video/sucai/transition/" + transitions[1] + '.glsl'

    video_clip = VideoFileClip(video_path)
    width, height = video_clip.size
    duration = video_clip.duration
    start_time = []
    start = round(random.uniform(2, 4), 2)
    head_cmd = f"""/home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i {video_path} -filter_complex " """
    num = 0
    while start < duration:
        start_time.append(start)
        next_start = round(start + round(random.uniform(2, 4), 2), 2)
        if num == 0:
            cmd = f"""[{num}:v]split=2[s0][s1];[s0][s1]gltransition=duration=2:offset={start}:source={transition}[{num}v]; """
            head_cmd += cmd
        else:
            if next_start > duration:
                cmd = f"""[{num - 1}v][0:v]gltransition=duration=2:offset={start}:source={transition} """
            else:
                cmd = f"""[{num - 1}v][0:v]gltransition=duration=2:offset={start}:source={transition}[{num}v]; """
            head_cmd += cmd
        start = next_start
        num += 1
    tail_cmd = f""" " -c:v libx264 -c:a aac -pix_fmt yuv420p -y {video_out} """
    head_cmd += tail_cmd
    print(head_cmd)
    print(start_time)
    # res = subprocess.run(head_cmd, shell=True)
    # if res.returncode == 0:
    #     print("success")
    print("耗时:", (datetime.datetime.now() - begin_time).seconds, "s")


def plusglshade(video_path):
    begin_time = datetime.datetime.now()
    video_out = video_path + ".texiao.mp4"
    names = ['split_4_', 'star_', 'mirror_', 'sway_', 'jitter_', 'preview_', 'soul_',
             'split_interval_', 'stab_ci_', 'test_', 'white_mask_', 'split_9_', 'split_vert2_']
    video_clip = VideoFileClip(video_path)
    width, height = video_clip.size
    duration = video_clip.duration
    # 480s
    start_times = []
    start = round(random.uniform(5, 10), 2)
    head_cmd = f"""xvfb-run -a --server-args="-screen 0 {width}x{height}x24 -ac -nolisten tcp -dpi 96 +extension RANDR" /home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i {video_path} -filter_complex " """
    num = 0
    while start < duration:
        start_times.append(start)
        name = random.choice(names)
        next_start = round(start + round(random.uniform(5, 10), 2), 2)
        if num == 0:
            head_cmd += f"""[{num}:v]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:start={start}:duration=5[{num}v]; """
        else:
            if next_start > duration:
                head_cmd += f"""[{num - 1}v]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:start={start}:duration=5"""
            else:
                head_cmd += f"""[{num - 1}v]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:start={start}:duration=5[{num}v]; """
        start = next_start
        num += 1
    tail_cmd = f""" " -c:v libx264 -c:a aac -pix_fmt yuv420p -y {video_out} """
    head_cmd += tail_cmd
    print(head_cmd)
    print(start_times)
    res = subprocess.run(head_cmd, shell=True)
    if res.returncode == 0:
        print("success")
    print("耗时:", (datetime.datetime.now() - begin_time).seconds, "s")

def gltansition_plusglshade(video_path):
    # 错误的
    # xvfb-run -a --server-args="-screen 0 576x1024x24 -nolisten tcp -dpi 96 +extension RANDR" /home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i video6.mp4 -filter_complex " [0:v]split=2[s0][s1];[s0][s1]gltransition=duration=2:offset=16.32:source=crosswarp.glsl[sv];[sv]plusglshader=sdsource=gl/sway_shader.gl:vxsource=gl/sway_vertex.gl:start=11.32:duration=5[0v]; [0v][0:v]gltransition=duration=2:offset=23.83:source=crosswarp.glsl,plusglshader=sdsource=gl/split_9_shader.gl:vxsource=gl/split_9_vertex.gl:start=18.83:duration=5[1v]; [1v][0:v]gltransition=duration=2:offset=35.36:source=crosswarp.glsl,plusglshader=sdsource=gl/white_mask_shader.gl:vxsource=gl/white_mask_vertex.gl:start=30.36:duration=5 " -c:v libx264 -c:a aac -pix_fmt yuv420p -y video6.mp4.tans_shade.mp4
    # RANDER
    # xvfb-run -a --server-args="-screen 0 576x1024x24 -ac -nolisten tcp -dpi 96 +extension RANDR" /home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i video6.mp4 -filter_complex " [0:v]split=2[s0][s1];[s0][s1]gltransition=duration=2:offset=17.310000000000002:source=crosswarp.glsl[sv];[sv]plusglshader=sdsource=gl/split_vert2_shader.gl:vxsource=gl/split_vert2_vertex.gl:start=12.31:duration=5[0v]; [0v][0:v]gltransition=duration=2:offset=28.14:source=crosswarp.glsl[0sv];[0sv]plusglshader=sdsource=gl/split_interval_shader.gl:vxsource=gl/split_interval_vertex.gl:start=23.14:duration=5[1v]; [1v][0:v]gltransition=duration=2:offset=39.18:source=crosswarp.glsl[1sv];[1sv]plusglshader=sdsource=gl/stab_ci_shader.gl:vxsource=gl/stab_ci_vertex.gl:start=34.18:duration=5 " -c:v libx264 -c:a aac -pix_fmt yuv420p -y video6.mp4.tans_shade.mp4
    # GLX
    # xvfb-run -a --server-args="-screen 0 576x1024x24 -ac -nolisten tcp -dpi 96 +extension GLX" /home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i video6.mp4 -filter_complex " [0:v]split=2[s0][s1];[s0][s1]gltransition=duration=2:offset=14.96:source=crosswarp.glsl[sv];[sv]plusglshader=sdsource=gl/test_shader.gl:vxsource=gl/test_vertex.gl:start=9.96:duration=5[0v]; [0v][0:v]gltransition=duration=2:offset=26.98:source=crosswarp.glsl[0sv];[0sv]plusglshader=sdsource=gl/star_shader.gl:vxsource=gl/star_vertex.gl:start=21.98:duration=5[1v]; [1v][0:v]gltransition=duration=2:offset=38.27:source=crosswarp.glsl[1sv];[1sv]plusglshader=sdsource=gl/jitter_shader.gl:vxsource=gl/jitter_vertex.gl:start=33.27:duration=5 " -c:v libx264 -c:a aac -pix_fmt yuv420p -y video6.mp4.tans_shade.mp4
    begin_time = datetime.datetime.now()
    video_out = video_path + ".tans_shade.mp4"
    names = ['split_4_', 'star_', 'mirror_', 'sway_', 'jitter_', 'preview_', 'soul_',
             'split_interval_', 'stab_ci_', 'test_', 'white_mask_', 'split_9_', 'split_vert2_']
    video_clip = VideoFileClip(video_path)
    width, height = video_clip.size
    duration = video_clip.duration
    # 480s
    start_times = []
    start = round(random.uniform(7.5, 12.5), 2)
    head_cmd = f"""xvfb-run -a --server-args="-screen 0 {width}x{height}x24 -ac -nolisten tcp -dpi 96 +extension RANDR" /home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i {video_path} -filter_complex " """
    num = 0
    while start < duration:
        start_times.append(start)
        name = random.choice(names)
        next_start = round(start + round(random.uniform(7.5, 12.5), 2), 2)
        if num == 0:
            head_cmd += f"""[0:v]split=2[s0][s1];[s0][s1]gltransition=duration=2:offset={start+5}:source=crosswarp.glsl[sv];[sv]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:start={start}:duration=5[{num}v]; """
        else:
            if next_start > duration:
                head_cmd += f"""[{num - 1}v][0:v]gltransition=duration=2:offset={start+5}:source=crosswarp.glsl[{num - 1}sv];[{num - 1}sv]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:start={start}:duration=5"""
            else:
                head_cmd += f"""[{num - 1}v][0:v]gltransition=duration=2:offset={start+5}:source=crosswarp.glsl[{num - 1}sv];[{num - 1}sv]plusglshader=sdsource=gl/{name}shader.gl:vxsource=gl/{name}vertex.gl:start={start}:duration=5[{num}v]; """
        start = next_start
        num += 1
    tail_cmd = f""" " -c:v libx264 -c:a aac -pix_fmt yuv420p -y {video_out} """
    head_cmd += tail_cmd
    print(head_cmd)
    print(start_times)
    # res = subprocess.run(head_cmd, shell=True)
    # if res.returncode == 0:
    #     print("success")
    print("耗时:", (datetime.datetime.now() - begin_time).seconds, "s")

def gltransition2(video_path,trans_time=None):
    begin_time = datetime.datetime.now()
    video_out = video_path + ".trans.mp4"
    transitions = ['Rolls.glsl', 'cube.glsl', 'wind.glsl', 'cannabisleaf.glsl', 'LinearBlur.glsl', 'powerKaleido.glsl', 'ripple.glsl', 'fadegrayscale.glsl', 'wipeRight.glsl', 'static_wipe.glsl', 'ZoomLeftWipe.glsl', 'BowTieVertical.glsl', 'luminance_melt.glsl', 'LeftRight.glsl', 'RotateScaleVanish.glsl', 'Dreamy.glsl', 'polar_function.glsl', 'wipeleft.glsl', 'SimpleZoomOut', 'squeeze.glsl', 'EdgeTransition.glsl', 'wipeLeft.glsl', 'circleopen.glsl', 'Overexposure.glsl', 'SimpleZoom.glsl', 'fadecolor.glsl', 'burn.glsl', 'randomNoisex.glsl', 'scale-in.glsl', 'BowTieHorizontal.glsl', 'randomsquares.glsl', 'Slides.glsl', 'squareswire.glsl', 'heart.glsl', 'multiply_blend.glsl', 'fade.glsl', 'colorphase.glsl', 'crosswarp.glsl', 'InvertedPageCurl.glsl', 'StaticFade.glsl', 'DreamyZoom.glsl', 'ZoomRigthWipe.glsl', 'Radial.glsl', 'BookFlip.glsl', 'DoomScreenTransition.glsl', 'displacement.glsl', 'windowslice.glsl', 'CircleCrop.glsl', 'wipeUp.glsl', 'pinwheel.glsl', 'CrossZoom.glsl', 'angular.glsl', 'tangentMotionBlur.glsl', 'RectangleCrop.glsl', 'HorizontalOpen.glsl', 'swap.glsl', 'BowTieWithParameter.glsl', 'VerticalOpen.glsl', 'PolkaDotsCurtain.glsl', 'Mosaic.glsl', 'HorizontalClose.glsl', 'doorway.glsl', 'circle.glsl', 'rotate_scale_fade.glsl', 'flyeye.glsl', 'WaterDrop.glsl', 'VerticalClose.glsl', 'x_axis_translation.glsl', 'TopBottom.glsl', 'wipeDown.glsl', 'ZoomInCircles.glsl', 'ButterflyWaveScrawler.glsl', 'morph.glsl']
    video_clip = VideoFileClip(video_path)
    duration = video_clip.duration
    if not trans_time:
        trans_time = []
        start = round(random.uniform(2, 5), 2)
        while start < duration:
            trans_time.append(round(start,2))
            start += random.uniform(2, 5)
    head_cmd = f"""/home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i {video_path} -filter_complex " """
    num = 0
    print(trans_time)
    for start in trans_time:
        transition = "sucai/transition/" + random.sample(transitions, 1)[0]
        if num == 0:
            cmd = f"""[{num}:v]split=2[s0][s1];[s0][s1]gltransition=duration=2:offset={start}:source={transition}[{num}v]; """
            head_cmd += cmd
        else:
            if num == len(trans_time)-1:
                cmd = f"""[{num - 1}v][0:v]gltransition=duration=2:offset={start}:source={transition} """
            else:
                cmd = f"""[{num - 1}v][0:v]gltransition=duration=2:offset={start}:source={transition}[{num}v]; """
            head_cmd += cmd
        num += 1
    tail_cmd = f""" " -c:v libx264 -c:a aac -pix_fmt yuv420p -y {video_out} """
    head_cmd += tail_cmd
    print(head_cmd)

    res = subprocess.run(head_cmd, shell=True)
    if res.returncode == 0:
        print("success")
    print("耗时:", (datetime.datetime.now() - begin_time).seconds, "s")
# plusglshade("input.mp4")
# gltransition("111.mp4")
# gltansition_plusglshade("video6.mp4")
gltransition2("111.mp4")
# names = ['split_4_', 'star_', 'mirror_', 'sway_', 'jitter_', 'preview_', 'soul_',
#          'split_interval_', 'stab_ci_', 'test_', 'white_mask_', 'split_9_', 'split_vert2_']
#
# name = random.choice(names)
# print(name)
