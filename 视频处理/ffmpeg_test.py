import ffmpy3
ff = ffmpy3.FFmpeg(
    inputs={'./demo.mp4': None},
    outputs={'output.avi': None}
)
ff.run()
