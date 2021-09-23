import subprocess
from sounddevice_instructions import get_output_device_id_by_name
import threading

"""
注：只有用多进程，才能实现多声道同时播放不同音频，一个进程调用一个sounddevice，占用一个声卡声道；
调用这几个子进程的时候，可以用多线程
"""
channel1 = "扬声器 (Realtek(R) Audio)"
channel2 = "耳机 (Realtek(R) Audio)"

channel_id_1 = str(get_output_device_id_by_name(channel1))
channel_id_2 = str(get_output_device_id_by_name(channel2))

audio_file1 = r"D:\PyCharm_Code\Python\audio\sox\聽海-張惠妹.wav"
audio_file2 = r"D:\PyCharm_Code\Python\audio\sox\千千阕歌-张国荣.wav"

cmd1 = "python sounddevice_instructions.py" + " " + audio_file1 + " " + channel_id_1 + " 2 44100"
print(cmd1)
cmd2 = "python sounddevice_instructions.py" + " " + audio_file2 + " " + channel_id_2 + " 2 44100"

# 使用多进程，同时使用两个声道，播放不同音频
def multi_channels_play1():
    print("channel_id1:", channel_id_1)
    subprocess.run(cmd1, shell=True)


def multi_channels_play2():
    print("channel_id2:", channel_id_2)
    subprocess.run(cmd2, shell=True)



if __name__ == '__main__':
    t1 = threading.Thread(target=multi_channels_play1)
    t2 = threading.Thread(target=multi_channels_play2)
    t1.start()
    t2.start()