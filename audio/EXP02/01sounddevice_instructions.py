"""
音频处理基本介绍
参考文档：Python 音频库 及具体使用介绍(包括声卡通道获取及选择) 第一篇: sounddevice -- by 七杀佩刃
网址：https://blog.csdn.net/weixin_42019925/article/details/96030954

"""
import os
import sys
import time
import wave
import numpy as np
import threading
import array
import sounddevice as sd
from scipy.io import wavfile
import soundfile as sf
import subprocess

class MyException(Exception):
    """自定义的异常类"""
    def __init__(self, *args):
        self.args = args

def preliminary_instruction():
    """
    初步说明 sounddevice查询声卡相关操作
    :return:
    """
    # 首先获取与当前主机连接的声卡设备驱动信息
    drivers_tuple = sd.query_hostapis()
    print("drivers_tuple", drivers_tuple) # 返回一个包含声卡驱动信息的元组, 元组的每个元素, 是一个个字典,
                                          # 包含了每个驱动的详细信息

    for driver_msg_dict in drivers_tuple:
        # 获取每个驱动的名字
        # MME, Windows DirectSound, ASIO, Windows WASAPI,  Windows WDM-KS
        print("driver: ", driver_msg_dict['name'], end=',')

        devices_list = sd.query_devices()    # 查询当前主机能用的声卡声道

        # 每个设备信息，以字典形式呈现
        for device_msg_dict in devices_list:
            print("device: ", device_msg_dict)


### 下面两个函数，是根据声卡声道名字，获取声卡声道名称及id，区分输出和输入两种声道 ###
def get_input_device_id_by_name(channel_name):
    """
    功能：根据声卡声道名字，获取输入声道id
    :param channel_name: 声道名称
    :return: 输入声道id
    """
    devices_list = sd.query_devices()
    for index, device_msg_dict in enumerate(devices_list):
        if channel_name == device_msg_dict['name'] and device_msg_dict['max_input_channels'] > 0:
            return index
        else:
            raise MyException("找不到该设备！！！")

def get_output_device_id_by_name(channel_name):
    """
    功能：根据声卡声道名字，获取输出声道id
    :param channel_name: 声道名称
    :return: 输出声道id
    """
    devices_list = sd.query_devices()
    for index, device_msg_dict in enumerate(devices_list):
        if channel_name == device_msg_dict["name"] and device_msg_dict['max_output_channels'] > 0:
            return index
    else:
        raise MyException("找不到该设备！！！")


def read_data(audio_file_path, audio_channels):
    # wav格式文件与raw(pcm)格式区分开，不同格式，获取其数据内容的方式不一样
    if audio_file_path.endswith(".wav"):
        data_array, samplerate = sf.read(audio_file_path)
        return data_array
    elif audio_file_path.endswith(".pcm") or audio_file_path.endswith(".raw"):
        # 打开一个音频文件，以raw(pcm)格式为例
        data_array = array.array('h')
        with open(audio_file_path, "rb") as f:
            data_array.frombytes(f.read())
            #  根据声道数，来进行切分
        data_array = data_array[::audio_channels]    # 有几个声道，切分的步长就是几，这样就单独切出一个声道
        return data_array


def play_audio_file(audio_file_path, channel_id, audio_channels, sample_rate):
    """
    将本机默认的声道改为自己设定的声道
    :param audio_file_path:
    :param channel_id:
    :param audio_channels:
    :param sample_rate:
    :return:
    """
    # sd.default.device 是一个列表, 第一个元素是: 默认的输入设备id; 第二个是默认的输出设备id
    sd.default.device[1] = channel_id

    data_array = read_data(audio_file_path, audio_channels)
    # 常选参数，一个数据，一个采样率，
    # 另外还有一个：blocking=True，若设置，则表示播放完毕当前音频再往下进行程序
    sd.play(data_array, sample_rate)
    # sd.wait()    # 表示等到此音频文件播放完毕后再往下执行程序
    # time.sleep(20)    # 休眠几秒，音频文件就播放几秒，时长自己控制
    # # 注：如果没有 类似休眠 等延时操作，则程序只会一闪而过，不会播放音频


# 使用sounddevice_example录制音频，提示也可以用多进程
def do_record(channel_id, file_path):
    # 首先设置默认录音声道id，id不同，调用的录音声卡也会不同，和播放一样，
    # 也支持多进程+多线程，多个声道同时录音
    sd.default.device[0] = channel_id

    # 再调用录音函数
    sample_rate = 44100    # 音频采样率
    length = 10    # 时长，单位秒
    record_data = sd.rec(frames=length*sample_rate, samplerate=sample_rate, channels=1, blocking=True)

    wavfile.write(file_path, sample_rate, record_data)


# 边录边播
def play_and_record(input_channel_id, output_channel_id, play_audio_file_path, rec_file_path,
                    play_audio_channels=1, play_audio_fs=44100, rec_file_channels=1):
    # 首先设置默认输出和输入声道
    sd.default.device[0] = input_channel_id
    sd.default.device[1] = output_channel_id

    # 开始边录边播
    data_array = read_data(play_audio_file_path, play_audio_channels)
    rec_data = sd.playrec(data=data_array, samplerate=play_audio_fs,
                          channels=rec_file_channels, blocking=True)

    # 存储录音文件
    wavfile.write(rec_file_path, play_audio_fs, rec_data)

####################### 多线程播放 #######################
def play_audio_1():
    file_path = r"D:\PyCharm_Code\Python\audio\sox\千千阕歌-张国荣.wav"
    output_id1 = get_output_device_id_by_name("扬声器 (Realtek(R) Audio)")
    print("扬声器声道：", output_id1)
    play_audio_file(file_path, channel_id=output_id1, audio_channels=2, sample_rate=44100)    # 只播放
    sd.wait()    # 等待音频文件播放完
    # time.sleep(10)

def play_audio_2():
    file_path = r"D:\PyCharm_Code\Python\audio\sox\喜欢你-邓紫棋.wav"
    output_id2 = get_output_device_id_by_name("耳机 (Realtek(R) Audio)")
    print("耳机声道：", output_id2)
    play_audio_file(file_path, channel_id=output_id2, audio_channels=2, sample_rate=44100)    # 只播放
    sd.wait()    # 等待音频文件播放完
    # time.sleep(10)
####################### 多线程播放 #######################

if __name__ == "__main__":
    preliminary_instruction()
####################### 多线程播放 #######################
    t1 = threading.Thread(target=play_audio_1)
    t1.start()
    t2 = threading.Thread(target=play_audio_2)
    t2.start()
####################### 多线程播放 #######################


"""
######################################### 单进程播放或录音 #########################################
    # file_path = r"D:\PyCharm_Code\Python\audio\sox\千千阕歌-张国荣.wav"
    # output_id = get_output_device_id_by_name("耳机 (Realtek(R) Audio)")
    # rec_file_path = os.getcwd() + "\\test_record.wav"    # os.getcwd()：返回当前进程的工作目录
    # input_id = get_input_device_id_by_name("麦克风阵列 (Realtek(R) Audio)")

    # play_audio_file(file_path, channel_id=output_id, audio_channels=1, sample_rate=44100)    # 只播放
    # sd.wait()    # 等待音频文件播放完
    # time.sleep(10)
    # do_record(channel_id=input_id, file_path=rec_file_path)    # 只录音

    # play_and_record(input_id, output_id, file_path, rec_file_path, play_audio_channels=2)    # 边录边播
######################################### 单进程播放或录音 #########################################



####################### 多进程播放 #######################
    # file_path = sys.argv[1]
    # output_id = int(sys.argv[2])
    # audio_channels = int(sys.argv[3])
    # fs = int(sys.argv[4])
    # play_audio_file(file_path, output_id, audio_channels, fs)    # 接收shell参数，多进程多声道播放音频
"""
