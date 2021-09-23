"""
将json格式或者protobuf格式的音频文件通过rabbit_mq接收并播放
"""
import pika
import audio_pb2 as pb
import io
import time
import soundfile
import sounddevice

### 连接rabbitmq服务器 ###
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

### 创建channel ###
channel =  connection.channel()

### 声明队列（queue） ###
channel.queue_declare(queue="泡沫")


### 定义一个回调函数，用来接收生产者发送的消息 ###
def callback(ch, method, properties, body):
    print("[*] Received the audio!")
    audio = pb.Audio()
    audio.ParseFromString(body)    # 反序列化
    data = audio.data
    # 方法一：先将内存中的数据写成wav文件，再用soundfile读取
    # with open("./rabbit_gem.wav", 'ab+') as f:
    #     f.write(data)

    # 方法二：不写成文件，用soundfile直接从内存中读取数据
    audio = io.BytesIO(data)

    audio_data, samplerate = soundfile.read(audio)
    sounddevice.play(audio_data, samplerate=samplerate)
    time.sleep(240)
    print("音频已播放完毕！")

### 订阅消费者 ###
channel.basic_consume(on_message_callback=callback,
                      queue="泡沫",
                      auto_ack=True)

### 开始消费：循环取消息 ###
channel.start_consuming()