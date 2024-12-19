import datetime
import os
import subprocess


def exe(file):
    cmd = f"""ffmpeg -loglevel quiet -i zimu6.mp4 -i video6.mp4 -filter_complex "gltransition=duration=4:offset=1:source=./ai_video/sucai/transition/{file}" -y ./trans/{file}.mp4 """
    try:
        print(cmd)
        res = subprocess.run(cmd, shell=True)
        if res.returncode != 0:
            print("error:", file)
    except Exception as e:
        print(e)


def test():
    directory = "./ai_video/sucai/transition/"
    files = []
    try:
        # 获取目录下的所有文件和文件夹名称
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry.name)
                    # start = datetime.datetime.now()
                    # exe(entry.name)
                    # print("耗时:", (datetime.datetime.now() - start).seconds)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied: {directory}")
    print(files)


test()

# aa = ['Rolls.glsl', 'cube.glsl', 'CrazyParametricFun.glsl', 'wind.glsl', 'cannabisleaf.glsl', 'LinearBlur.glsl', 'pixelize.glsl', 'perlin.glsl', 'powerKaleido.glsl', 'ripple.glsl', 'GlitchDisplace.glsl', 'fadegrayscale.glsl', 'directionalwipe.glsl', 'wipeRight.glsl', 'static_wipe.glsl', 'directionalwarp.glsl', 'ZoomLeftWipe.glsl', 'StereoViewer.glsl', 'TVStatic.glsl', 'Bounce.glsl', 'windowblinds.glsl', 'rotateTransition.glsl', 'Directional.glsl', 'BowTieVertical.glsl', 'GridFlip.glsl', 'luminance_melt.glsl', 'LeftRight.glsl', 'Swirl.glsl', 'RotateScaleVanish.glsl', 'Dreamy.glsl', 'polar_function.glsl', 'wipeleft.glsl', 'SimpleZoomOut', 'squeeze.glsl', 'EdgeTransition.glsl', 'wipeLeft.glsl', 'hexagonalize.glsl', 'circleopen.glsl', 'Overexposure.glsl', 'FilmBurn.glsl', 'SimpleZoom.glsl', 'fadecolor.glsl', 'burn.glsl', 'randomNoisex.glsl', 'scale-in.glsl', 'BowTieHorizontal.glsl', 'randomsquares.glsl', 'Slides.glsl', 'squareswire.glsl', 'heart.glsl', 'multiply_blend.glsl', 'fade.glsl', 'colorphase.glsl', 'crosswarp.glsl', 'InvertedPageCurl.glsl', 'StaticFade.glsl', 'DreamyZoom.glsl', 'luma.glsl', 'ZoomRigthWipe.glsl', 'Radial.glsl', 'BookFlip.glsl', 'DoomScreenTransition.glsl', 'displacement.glsl', 'windowslice.glsl', 'CircleCrop.glsl', 'wipeUp.glsl', 'pinwheel.glsl', 'CrossZoom.glsl', 'angular.glsl', 'tangentMotionBlur.glsl', 'RectangleCrop.glsl', 'undulatingBurnOut.glsl', 'HorizontalOpen.glsl', 'swap.glsl', 'mosaic_transition.glsl', 'BowTieWithParameter.glsl', 'VerticalOpen.glsl', 'coord-from-in.glsl', 'PolkaDotsCurtain.glsl', 'Mosaic.glsl', 'HorizontalClose.glsl', 'directional-easing.glsl', 'doorway.glsl', 'circle.glsl', 'rotate_scale_fade.glsl', 'flyeye.glsl', 'WaterDrop.glsl', 'ColourDistance.glsl', 'crosshatch.glsl', 'VerticalClose.glsl', 'x_axis_translation.glsl', 'TopBottom.glsl', 'wipeDown.glsl', 'DirectionalScaled.glsl', 'kaleidoscope.glsl', 'GlitchMemories.glsl', 'ZoomInCircles.glsl', 'Rectangle.glsl', 'ButterflyWaveScrawler.glsl', 'morph.glsl']
# print(len(aa))
