import subprocess


def divide_voice(audio_file):
    # spleeter = "/home/ubuntu/miniconda3/envs/test/bin/spleeter"
    spleeter = "spleeter"
    cmd = f"""{spleeter} separate --verbose -p spleeter:2stems -o ./tmp_audio/ {audio_file}"""
    print(cmd)
    res = subprocess.run(cmd, shell=True)
    if res.returncode == 0:
        vocals_path = "./tmp_audio/" + audio_file.split(".")[0] + "/vocals.wav"
        accompaniment_path = "./tmp_audio/" + audio_file.split(".")[0] + "/accompaniment.wav"
        return vocals_path, accompaniment_path
    else:
        print("分离音频中的人声和背景声失败")
        return None, None

if __name__ == "__main__":
    for i in range(2,33):
        audio_file = './mp3/'+str(i)+".mp3"
        print(divide_voice(audio_file))
