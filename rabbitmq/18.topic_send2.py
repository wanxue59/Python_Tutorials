"""
参考文档：python实现RabbitMQ六种模式 --  by The_shy等风来
网址：https://blog.csdn.net/qq_37623764/article/details/105767004
topic--生产者
"""
import pika

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='topic_logs2', exchange_type='topic')

# 创建纯文本消息
message  = "Welcome to rabbitmq lyc."

### 将消息发送到RabbitMQ ###
channel.basic_publish(exchange='topic_logs2',
                      routing_key='lan.adasd.*',
                      body=message)
print("Sent {} successfully.".format(message))

### 关闭与rabbit的连接 ###
connection.close()