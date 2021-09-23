import numpy as np
import time
import soundfile as sf
import sounddevice as sd

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

# sr=None声音保持原采样频率
# data, samplerate = librosa.load(r'D:\PyCharm_Code\Python\audio\sox\GEM.wav', sr=None, mono=False)
# # mono=False声音保持原通道数
# print('librosa.load 声音数据的维度: {}\n数据类型: {}\n最大值: {}\n中间值: {}\n最小值: {}\n采样率：{}'\
#       .format(data.shape, data.dtype, np.max(data), np.median(data), np.min(data), samplerate))
preliminary_instruction()
# data, samplerate = sf.read(r'D:\PyCharm_Code\Data\audio\聽海-張惠妹.wav')
data, samplerate = sf.read(r'D:\PyCharm_Code\Data\audio\千千阕歌-张国荣.wav')
print('librosa.load 声音数据的维度: {}\n数据类型: {}\n最大值: {}\n中间值: {}\n最小值: {}\n采样率：{}'\
      .format(data.shape, data.dtype, np.max(data), np.median(data), np.min(data), samplerate))
# 常选参数，一个数据，一个采样率，
# 另外还有一个：blocking=True，若设置，则表示播放完毕当前音频再往下进行程序
sd.play(data, samplerate)
# sd.wait()    # 表示等到此音频文件播放完毕后再往下执行程序
time.sleep(400)    # 休眠几秒，音频文件就播放几秒，时长自己控制
# 注：如果没有类似休眠等延时操作，则程序只会一闪而过，不会播放音频