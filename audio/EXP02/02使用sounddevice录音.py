# coding: utf8

"""
    Python 音频: 使用 sounddevice 操作声卡的 左声道, 右声道, 立体声
    仅限 MME,   Windows DirectSound,   Windows WASAPI,   Windows WDM-KS 等支持双声道的驱动类型
"""

import os
import sounddevice as sd
import soundfile

mapping_left_ch = 1  # 左声道为 1
mapping_right_ch = 2  # 右声道为 2
mapping_stereo = None  # 立体声为 None

"""
   0 Microsoft 声音映射器 - Input, MME (2 in, 0 out)
>  1 麦克风阵列 (Realtek High Defini, MME (2 in, 0 out)
   2 Microsoft 声音映射器 - Output, MME (0 in, 2 out)
<  3 扬声器 (Realtek High Definition, MME (0 in, 2 out)
   4 PHL 230B8Q (英特尔(R) 显示器音, MME (0 in, 2 out)
   5 主声音捕获驱动程序, Windows DirectSound (2 in, 0 out)
   6 麦克风阵列 (Realtek High Definition Audio), Windows DirectSound (2 in, 0 out)
   7 主声音驱动程序, Windows DirectSound (0 in, 2 out)
   8 扬声器 (Realtek High Definition Audio), Windows DirectSound (0 in, 2 out)
   9 PHL 230B8Q (英特尔(R) 显示器音频), Windows DirectSound (0 in, 2 out)
  10 PHL 230B8Q (英特尔(R) 显示器音频), Windows WASAPI (0 in, 2 out)
  11 扬声器 (Realtek High Definition Audio), Windows WASAPI (0 in, 2 out)
  12 麦克风阵列 (Realtek High Definition Audio), Windows WASAPI (2 in, 0 out)
  13 Output (英特尔(R) 显示器音频 - 输出 1.1), Windows WDM-KS (0 in, 2 out)
  14 Speakers 1 (Realtek HD Audio output with SST), Windows WDM-KS (0 in, 2 out)
  15 Speakers 2 (Realtek HD Audio output with SST), Windows WDM-KS (0 in, 6 out)
  16 电脑扬声器 (Realtek HD Audio output with SST), Windows WDM-KS (2 in, 0 out)
  17 麦克风阵列 1 (), Windows WDM-KS (2 in, 0 out)
  18 麦克风阵列 2 (), Windows WDM-KS (1 in, 0 out)
"""

# 此文件是双声道, 44100采样率
test_wav_file_path = r'D:\PyCharm_Code\Data\audio\千千阕歌-张国荣.wav'

# 初始化一个录音文件路径
rec_file_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)),
                             "sounddevice_test_wav", "rec_files"+"\\")
if not os.path.exists(rec_file_dir):
    os.makedirs(rec_file_dir)
rec_file_path = rec_file_dir + "rec_test1.wav"
if not exit(rec_file_path):
    os.mkdir(rec_file_path)

# 播放文件读取一下, 获取到numpy数组和采样率,
# 这里我为了节省时间, 只读了一部分, 采样率为 44100, 我只读10秒, 为441000个点
# to_play_data_array, sample_rate = soundfile.read(test_wav_file_path, stop=44100*10)


def play_by_left_ch():
    """
    功能: 左声道播放
    :return:
    """

    sd.default.device[1] = 8  # 本机使用索引为8的声卡通道来播放

    # 使用左/右声道播放, 只支持单通道的音频文件, 否则会报错
    left_ch_data_array = to_play_data_array.T[0]  # 矩阵转置一下, 得到第一个声道的数据

    # 单独使用左声道, 验证听了, 确实是左声道
    sd.play(left_ch_data_array, blocking=True, samplerate=sample_rate, mapping=mapping_left_ch)


def play_by_right_ch():
    """
    功能: 右声道播放
    :return:
    """

    sd.default.device[1] = 8  # 使用索引为8的声卡通道来播放

    # 使用左/右声道播放, 只支持单通道的音频文件, 否则会报错
    right_ch_data_array = to_play_data_array.T[1]  # 得到第二个声道的数据

    # 单独使用右声道, 验证听了, 确实是右声道
    sd.play(right_ch_data_array, blocking=True, samplerate=sample_rate, mapping=mapping_right_ch)


def play_by_stereo():
    """
    功能: 立体声播放
    :return:
    """

    sd.default.device[1] = 8  # 使用索引为8的声卡通道来播放
    # 双声道就用立体声
    sd.play(to_play_data_array, blocking=True, samplerate=sample_rate, mapping=mapping_stereo)


def rec_by_left_ch():
    """
    功能: 左声道录音
    :return: 录音结果数据
    """

    """
    注意: 
       如果用左声道/右声道, 那么, channels 必须为 1, 否则会报错
       如果使用立体声, 声道数量可以为1, 也可以为2, 但如果大于2, 也会报错
    """

    # 录音测试
    sd.default.device[0] = 6  # 使用索引为6的声卡通道来录音
    res_data_array = sd.rec(frames=48000 * 10, samplerate=48000, channels=1,
                            mapping=mapping_left_ch, blocking=True)

    return res_data_array


def rec_by_right():
    """
    功能: 右声道录音
    :return: 录音结果数据
    """

    """
    注意: 
        如果用左声道/右声道, 那么, channels 必须为 1, 否则会报错
        如果使用立体声, 声道数量可以为1, 也可以为2, 但如果大于2, 也会报错
    """

    sd.default.device[0] = 6  # 使用索引为6的声卡通道来录音
    res_data_array = sd.rec(frames=48000 * 10, samplerate=48000, channels=1,
                            mapping=mapping_right_ch, blocking=True)

    return res_data_array


def play_and_rec():
    """
    功能: 边播边录
    :return: 录音结果数据
    """

    sd.default.device[0] = 6  # 使用索引为6的声卡通道来录音
    sd.default.device[1] = 8  # 使用索引为8的声卡通道来播放

    # 测试边播放边录音
    # 录音文件的采样率和采样点数, 都和播放文件的一样
    res_data_array = sd.playrec(to_play_data_array, samplerate=sample_rate, blocking=True,
                                input_mapping=mapping_stereo, output_mapping=mapping_stereo,
                                channels=2)

    return res_data_array


def write_to_wav_file(res_data_array):
    """
    功能: 将录音数据写入文件
    :param res_data_array: 录音结果数据
    :return:
    """

    # 保存
    # 这里写入文件使用的采样率最好和录音得到的res_data_array一样, 否则会造成文件时长和录音设定的不一样
    # 如果采样率不一致, 文件也会异常, 听着不对
    soundfile.write(rec_file_path, res_data_array, samplerate=sample_rate, subtype="PCM_16")


if __name__ == "__main__":
    data_array = play_and_rec()
    write_to_wav_file(data_array)

    # 获取一下录制文件的信息
    s = soundfile.SoundFile(rec_file_path)
    print(s.frames)  # 总帧数, 也就是总的采样点数(每个声道的点数一样, 每个声道都是这个数)
    print(s.channels)  # 声道数
    print(s.subtype)  # 数据类型, soundfile 自己定义的类型, 可以和numpy的数据类型对应起来
    print(s.samplerate)  # 采样率
    print(s.frames/s.samplerate)  # 计算时长, 单位: 秒

