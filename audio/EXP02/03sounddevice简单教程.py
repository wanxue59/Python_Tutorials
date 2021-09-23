import sounddevice
devices = sounddevice.query_devices()    # 返回所有设备信息
print("device:\n", devices)    # 打印所有设备信息
# input_devices = sounddevice.query_devices(kind='input')    # 返回所有输入设备信息
# print("input_device:\n", input_devices)    # 打印所有输入设备信息
# output_devices = sounddevice.query_devices(kind='output')    # 返回所有输出设备信息
# print("output_device:\n", output_devices)    # 打印所有输出设备信息
default_device = sounddevice.default.device    # 返回默认声卡设备信息
print("default_device:\n", default_device)    # 打印默认声卡设备信息


# for i, device in enumerate(devices):
#     if device['max_output_channels'] > 0 and 'USB' in device['name']:
#         print(i)