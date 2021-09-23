import test_pb2

### 对protobuf中的各种变量进行赋值 ###
testinfo = test_pb2.testinfo()    # 类似类的实例化
testinfo.devtype = 100    # 类似“实例.属性”的方式进行赋值
testinfo.devid = 2
testinfo.unitid = 3
testinfo.chlid = 4
testinfo.testid = 5
testinfo.stepdata = b"abd"

print("protobuf结构的内容：")
print(testinfo, testinfo.devtype, "\n")    # 打印protobuf结构的内容
out = testinfo.SerializeToString()    # 序列化：序列化此消息为二进制串
print("Protobuf序列字符串:")
print(out, "\n")    # 打印Protobuf序列字符串

decode = test_pb2.testinfo()
decode.ParseFromString(out)    # 解析函数
print("Protobuf解析后的内容:")
print(decode)    # 打印Protobuf解析后的内容