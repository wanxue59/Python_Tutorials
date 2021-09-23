"""
一个发消息，多个收消息，收消息是公平地依次分发
生产者：auto=False（自动应答关闭）
"""
import pika
import time
import sys
### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
### 创建一个AMQP信道（channel） ###
channel = connection.channel()
### 声明队列queue ###
channel.queue_declare(queue='task_queue')    # queue名为hello
### 生产一个消息 ###
message = "".join(sys.argv[1:]) or "1Hello World! {}".format(time.time())
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))    # 消息持久化；默认为1，不持久化
print("[x] Sent {}".format(message))
### 关闭与rabbit的连接 ###
connection.close()