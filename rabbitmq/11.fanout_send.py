"""
    fanout广播模式：所有绑定exchange的queue都可以接收到消息。exchange=>转换器
    消息被所有的queue接收，广播是实时的，你不在的时候，就是你消费者没有开启的时候，发消息的时候，就没有收到，这个时候就
没有了。如果消费者开启了，生产者发消息时，消费者是收的到的，这个又叫订阅发布，收音机模式
"""
import pika
import sys

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='logs', exchange_type='fanout')    # 发送消息类型为fanout,就是给所有人发消息

# 创建纯文本消息
message = ''.join(sys.argv[1:]) or "info: Hello World!"    # 如果等于空，就输出Hello World!

### 将消息发送到RabbitMQ ###
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print("[x] Sent %r"%message)

### 关闭与rabbit的连接 ###
connection.close()