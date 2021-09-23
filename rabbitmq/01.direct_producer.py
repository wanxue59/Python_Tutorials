"""生产者"""
import pika
### 连接rabbitmq服务器 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
### 创建一个AMQP信道（channel） ###
channel = connection.channel()
### 声明队列queue ###
channel.queue_declare(queue='hello')    # queue名为hello
### 发送消息 ###
# 如果exchange为空，即简单模式
# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
channel.basic_publish(exchange='',
                      routing_key='hello',    # queue的名字
                      body='Hello World!')    # 具体的消息内容
print("[x] Sent 'Hello World!'")
###  关闭与rabbitmq的连接 ###
connection.close()    # 直接关闭连接