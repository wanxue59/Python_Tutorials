import sounddevice as sd
import wave
import time
import os
import numpy as np
from array import array
from struct import pack
import serial
# import serial.tools.list_ports
import contextlib

stream = None
raw_data = np.empty(shape=(0, 1), dtype=np.int16)
print("len(raw_data): ", len(raw_data))
print(raw_data.shape)

# print(len(raw_data))
ser = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)
# print(sd.query_devices())
# print(sd.default.device)
stream = sd.Stream(samplerate=8000,
                   blocksize=1024,
                   device=sd.default.device,
                   channels=1,
                   dtype=np.dtype(np.int16))
stream.start()



def record_to_file(path, data, sample_width):
    "Records from the microphone and outputs the resulting data to 'path'"
    # 录音文件上下限保护
    timespan = len(data) * 1.0 / 16000
    if timespan > 15.0 or timespan < 1.0:
        return
    # data = pack('<' + ('h'*len(data)), *data)    # 将数据打包
    wf = wave.open(path, 'wb')
    wf.setnchannels(1)    # 设置声道数为1
    wf.setsampwidth(sample_width)    # 设置采样字节长度为sample_width
    wf.setframerate(8000)    # 设置采样频率为8000

    wf.writeframes(data)  # 将音频数据流数据写入wave文件
    wf.close()


while True:
    if not ser.getCTS():    # 通话按钮被按下时  CTS：Clear To Send 清除发送  getCTS：返回CTS线路的状态
        if len(raw_data) == 0:
            print("Starting fetching speech")
        data_buffer = stream.read(1024)
        print(type(data_buffer[0]))
        # raw_data = np.frombuffer(data_buffer[0])
        raw_data = np.concatenate((raw_data, data_buffer[0]))
        # print('data_buffer: ', data_buffer)
        print('raw_data: ', raw_data)

    else:  # 通话按钮被松开时
        # print(raw_data)
        if len(raw_data) == 0:  # 表示此前通话按钮一直是松开的
            time.sleep(0.02)
            continue  # 继续检测

        pathname = r"D:\PyCharm_Code\Tutorials\audio\sounddevice_test_wav\rec_files"  # 存储音频文件的目录
        if not os.path.exists(pathname):
            os.makedirs(pathname)
        filename = "ZUUU" + ".wav"  # 音频文件名
        file_dir = pathname + "\\" + filename  # 存储录音的音频文件的绝对路径
        # print('data_buffer: ', data_buffer)
        record_to_file(file_dir, raw_data, 2)
        print(len(raw_data))
        # np.delete(raw_data)

