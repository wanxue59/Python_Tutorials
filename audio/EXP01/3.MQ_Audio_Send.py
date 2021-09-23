"""
将音频文件读取并转成json格式或者protobuf格式，通过rabbit_mq发送
"""
import pika
import audio_pb2 as pb
import soundfile
import json
### 连接rabbitmq服务器 ###
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

### 创建一个AMQP信道（channel） ###
channel = connection.channel()

### 声明队列（queue） ###
channel.queue_declare(queue="泡沫")

### 读取音频，转为protbuf文件 ###
audio = pb.Audio()
file_path = r"D:\PyCharm_Code\Python\audio\sox\GEM.wav"
with open(file_path, 'rb') as f:
    # print(f.read())
    audio.data = f.read()


message = audio.SerializeToString()    # 序列化：序列化此消息为二进制串

## 发送消息 ###
channel.basic_publish(exchange='',
                      routing_key='泡沫',
                      body=message)
print("[x] Sent the audio!")

### 关闭与rabbitmq的连接 ###
# connection.close()