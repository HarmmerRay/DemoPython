import datetime
import random
import subprocess

from moviepy.video.io.VideoFileClip import VideoFileClip


def gltransition(video_path,trans_time=None):
    print("混剪结束，开始添加转场",video_path)
    begin_time = datetime.datetime.now()
    video_out = video_path + ".trans.mp4"
    transitions = ['Rolls.glsl', 'cube.glsl', 'wind.glsl', 'cannabisleaf.glsl', 'LinearBlur.glsl', 'powerKaleido.glsl',
                   'ripple.glsl', 'fadegrayscale.glsl', 'wipeRight.glsl', 'static_wipe.glsl', 'ZoomLeftWipe.glsl', 'BowTieVertical.glsl',
                   'luminance_melt.glsl', 'LeftRight.glsl', 'RotateScaleVanish.glsl', 'Dreamy.glsl', 'polar_function.glsl', 'wipeleft.glsl',
                   'SimpleZoomOut', 'squeeze.glsl', 'EdgeTransition.glsl', 'wipeLeft.glsl', 'circleopen.glsl', 'Overexposure.glsl',
                   'SimpleZoom.glsl', 'fadecolor.glsl', 'burn.glsl', 'randomNoisex.glsl', 'scale-in.glsl',
                   'randomsquares.glsl', 'Slides.glsl', 'squareswire.glsl', 'heart.glsl', 'multiply_blend.glsl', 'fade.glsl', 'colorphase.glsl',
                   'crosswarp.glsl', 'InvertedPageCurl.glsl', 'StaticFade.glsl', 'DreamyZoom.glsl', 'ZoomRigthWipe.glsl', 'Radial.glsl',
                   'BookFlip.glsl', 'DoomScreenTransition.glsl', 'displacement.glsl', 'windowslice.glsl', 'CircleCrop.glsl', 'wipeUp.glsl',
                   'CrossZoom.glsl', 'angular.glsl', 'tangentMotionBlur.glsl', 'RectangleCrop.glsl', 'HorizontalOpen.glsl',
                   'swap.glsl', 'VerticalOpen.glsl', 'Mosaic.glsl', 'HorizontalClose.glsl','doorway.glsl', 'circle.glsl',
                   'rotate_scale_fade.glsl', 'flyeye.glsl', 'WaterDrop.glsl', 'TopBottom.glsl', 'wipeDown.glsl', 'ZoomInCircles.glsl',
                   'ButterflyWaveScrawler.glsl', 'morph.glsl']
    video_clip = VideoFileClip(video_path)
    duration = video_clip.duration
    if not trans_time:
        trans_time = []
        # start = round(random.uniform(4, 8), 2)
        start = 4
        while start < duration:
            trans_time.append(round(start,2))
            start += 4
    count = 0
    while count < len(transitions):
        head_cmd = f"""/home/ubuntu/miniconda3/envs/test2/bin/ffmpeg -i {video_path} -filter_complex " """
        num = 0
        print(trans_time)

        for start in trans_time:
            transition = "ai_video/sucai/transition/" + transitions[count]
            count += 1
            if num == 0:
                cmd = f"""[{num}:v]split=2[s0][s1];[s0][s1]gltransition=duration=3:offset={start}:source={transition}[{num}v]; """
                head_cmd += cmd
            else:
                if num == len(trans_time)-1 or count >= len(transitions):
                    cmd = f"""[{num - 1}v][0:v]gltransition=duration=3:offset={start}:source={transition} """
                    head_cmd += cmd
                    break
                else:
                    cmd = f"""[{num - 1}v][0:v]gltransition=duration=3:offset={start}:source={transition}[{num}v]; """
                    head_cmd += cmd
            num += 1
        tail_cmd = f""" " -c:v libx264 -c:a aac -pix_fmt yuv420p -y {count}{video_out} """
        head_cmd += tail_cmd
        print(head_cmd)

        res = subprocess.run(head_cmd, shell=True)
        if res.returncode == 0:
            print("gl_transition成功！耗时:", (datetime.datetime.now() - begin_time).seconds, "s")
            # return video_out
        else:
            print("gl_transition失败！耗时:", (datetime.datetime.now() - begin_time).seconds, "s")
            # return video_path
    print("样式生成完成")
if __name__ == "__main__":
    # gltransition("22.mp4")
    aa = transitions = ['Rolls.glsl', 'cube.glsl','powerKaleido.glsl', 'fadegrayscale.glsl','LeftRight.glsl', 'RotateScaleVanish.glsl', 'Dreamy.glsl','SimpleZoomOut', 'squeeze.glsl','EdgeTransition.glsl',
                   'SimpleZoom.glsl',  'randomNoisex.glsl','scale-in.glsl', 'Slides.glsl','crosswarp.glsl', 'InvertedPageCurl.glsl',  'DreamyZoom.glsl','BookFlip.glsl', 'DoomScreenTransition.glsl',
                   'CircleCrop.glsl','RectangleCrop.glsl','Mosaic.glsl','doorway.glsl', 'circle.glsl','rotate_scale_fade.glsl','TopBottom.glsl','ZoomInCircles.glsl','ButterflyWaveScrawler.glsl',]
    print(len(aa))