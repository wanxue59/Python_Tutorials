"""
生产者
四、消息公平分发
    如果Rabbit只管按顺序把消息发到各个消费者身上，不考虑消费者负载的话，很可能出现，一个机器配置不高的消费者那里堆积了很
多消息处理不完，同时配置高的消费者却一直很轻松。为解决此问题，可以在各个消费者端，配置perfetch=1,意思就是告诉RabbitMQ在
我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
"""
import pika

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

### 创建一个AMQP信道（channel） ###
channel = connection.channel()

### 声明队列queue ###
channel.queue_declare(queue="durable_queue", durable=True)    # 队列持久化

### 生产一个消息并持久化 ###
message = "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='durable_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))    # 消息持久化
print("[x] Sent {}".format(message))

### 关闭与rabbit的连接 ###
connection.close()
