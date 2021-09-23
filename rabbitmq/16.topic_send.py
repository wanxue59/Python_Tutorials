"""
topic--生产者
发消息时指定关键字+消息，如：
python 17.topic_send.py info Hello World!
"""
import pika
import sys

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


routing_key = sys.argv[1] if len(sys.argv) > 1 else "anonymous.info"
# 创建纯文本消息
message = ''.join(sys.argv[2:]) or "Hello World!"

### 将消息发送到RabbitMQ ###
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print("[x] Sent {}: {}".format(routing_key, message))

### 关闭与rabbit的连接 ###
connection.close()