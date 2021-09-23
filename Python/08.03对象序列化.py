"""
导入pickle模块后，就可以实现pickle功能了。在pickle模块中，共有4个函数可以使用。
    ·dumps:将Python中的对象序列化成二进制对象，并返回。
    ·loads:从给定的pickle数据中读取并返回对象。
    ·dump:将Python中的对象序列化成二进制对象，并写入文件。
    ·load:读取指定的序列化数据文件，并返回对象。
这4个函数可以分成两类:dumps 与 loads,实现基于内存的Python对象与二进制互转；dump与load，实现基于文件的
Python对象与二进制互转。
"""
import json
import wave

tup1 = ("I love Python", [1, 2, 3], None)    # 定义一个含有复杂元素的元组
p1 = json.dumps(tup1)    # 将Python对象元组tup1转为二进制对象
t2 = json.loads(p1)    # 将二进制对象p1转为Python对象
print("tup1: ", tup1)
print("p1: ", p1)
print("t2: ", t2)


data_dir = r"D:\PyCharm_Code\Data\audio\喜欢你-邓紫棋.wav"
with open(data_dir, 'rb') as f:
    data = f.read()
print("data: ", data)
p2 = json.dump(data)
t3 = json.load(p2)
print("p2: ", p2)
print("t3: ", t3)