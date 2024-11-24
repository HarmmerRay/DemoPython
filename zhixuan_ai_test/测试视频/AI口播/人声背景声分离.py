import os
from spleeter.separator import Separator

# 输出目录
output_dir = './mp3_divide/'
os.makedirs(output_dir, exist_ok=True)

audio_file = './mp3/1.mp3'

# 初始化Spleeter分离器
separator = Separator('spleeter:2stems')

# 分离音频并保存结果
separator.separate_to_file(audio_file, output_dir)

print(f"分离完成，人声保存为 {os.path.join(output_dir, '1/vocals.wav')}，背景声保存为 {os.path.join(output_dir, '1/accompaniment.wav')}")