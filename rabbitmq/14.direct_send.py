"""
    direct广播模式：队列绑定关键字，发送者将数据根据关键字发送到消息exchange，exchange根据关键字判定应该将数据发送至指定
队列。
"""
import pika
import sys

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')


severity = sys.argv[1] if len(sys.argv) > 1 else 'info'    # 严重程序，级别；判定条件到底是info，还是空，后面接消息
message = ''.join(sys.argv[2:]) or "Hello World!"

### 将消息发送到RabbitMQ ###
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,    # 绑定的是：error指定关键字（哪些队列绑定了这个级别，那些队列就可以收到这个消息）
                      body=message)
print("[x] Sent %r"%message)

### 关闭与rabbit的连接 ###
connection.close()
