"""
消费者
四、消息公平分发
    如果Rabbit只管按顺序把消息发到各个消费者身上，不考虑消费者负载的话，很可能出现，一个机器配置不高的消费者那里堆积了很
多消息处理不完，同时配置高的消费者却一直很轻松。为解决此问题，可以在各个消费者端，配置perfetch=1,意思就是告诉RabbitMQ在
我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
"""
import pika
import time

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

### 创建一个AMQP信道（channel） ###
channel = connection.channel()

### 声明队列queue，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行 ###
channel.queue_declare(queue="durable_queue", durable=True)    # 队列持久化

print("[*] Waiting for messages. To exit press CTRL+C.")

### 定义一个回调函数，用来接收生产者发送的消息 ###
def callback(ch, method, properties, body):
    print("[x] Received {}".format(body))
    print("\tch: {};\n\tmethod: {};\n\tproperties: {}".format(ch, method, properties))
    time.sleep(body.count(b'.'))
    print("[x] Done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

### 订阅消费者 ###
channel.basic_qos(prefetch_count=1)    # 在消费者端，配置perfetch=1,表明消费者当前消息还没处理，不要再发新消息
channel.basic_consume(queue="durable_queue",    # 队列持久化
                      on_message_callback=callback)

### 开始消费：循环取消息 ###
channel.start_consuming()    # 启动消费模式