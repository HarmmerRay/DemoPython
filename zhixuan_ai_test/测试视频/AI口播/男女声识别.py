# 根据男声女声的音频频率不同，判断男女声
import librosa
import numpy as np
import matplotlib.pyplot as plt

def extract_fundamental_frequency(y, sr):
    # 提取基频
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
    return f0, voiced_flag

def classify_gender(f0, voiced_flag):
    # 过滤掉非语音段
    voiced_f0 = f0[voiced_flag > 0]

    if len(voiced_f0) == 0:
        return "无法确定"

    # 计算基频的平均值
    mean_f0 = np.mean(voiced_f0)

    # 根据基频的平均值判断性别
    if mean_f0 < 165:  # 男性基频通常低于165 Hz
        return "男性"
    else:
        return "女性"

def main(audio_file):


    # 加载音频文件
    y, sr = librosa.load(audio_file, sr=None)

    # 提取基频
    f0, voiced_flag = extract_fundamental_frequency(y, sr)

    # 分类性别
    gender = classify_gender(f0, voiced_flag)

    print(f"音频文件 {audio_file} 的性别是: {gender}")

    # 可视化基频
    # plt.figure(figsize=(10, 4))
    # plt.plot(f0, label='基频')
    # plt.xlabel('时间帧')
    # plt.ylabel('频率 (Hz)')
    # plt.title('基频随时间变化')
    # plt.legend()
    # plt.show()

if __name__ == "__main__":
    for i in range(1,22):
        audio_file = './mp3/'+str(i)+".mp3"
        main(audio_file)
