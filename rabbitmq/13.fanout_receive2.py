"""
    fanout广播模式：所有绑定exchange的queue都可以接收到消息。exchange=>转换器
    消息被所有的queue接收，广播是实时的，你不在的时候，就是你消费者没有开启的时候，发消息的时候，就没有收到，这个时候就
没有了。如果消费者开启了，生产者发消息时，消费者是收的到的，这个又叫订阅发布，收音机模式
"""
import pika

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(queue='', exclusive=True)    # 必须通过queue来接收消息

queue_name = result.method.queue    # 获取随机队列名称

### 将队列和交换器绑定 ###
channel.queue_bind(exchange='logs', queue=queue_name)    # 随机生成的队列，绑定到exchange上

print("[*] Waiting for logs. To exit press CTRL+C")

### 定义一个回调函数，用来接收生产者发送的消息 ###
def callback(ch, method, properties, body):
    print("[x] {}".format(body))

### 监听随机队列，一旦有值出现，则触发回调函数：callback ###
channel.basic_consume(queue=queue_name,
                      auto_ack=False,    # 默认就是False,可以直接不写
                      on_message_callback=callback)

### 开始消费：循环取消息 ###
channel.basic_qos(prefetch_count=1)    # perfetch=1表明消费者当前消息还没处理，不要再发新消息
channel.start_consuming()