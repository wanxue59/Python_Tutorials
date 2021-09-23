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
channel.exchange_declare(exchange='direct_log', exchange_type='direct')
# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue


severities = sys.argv[1:]    # 接收那些消息（指info，还是空），没写就报错
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n"%sys.argv[0])    # 定义了三种接收消息方式info,warning,error
    sys.exit(1)

### 将队列和交换器绑定 ###
for severity in severities:    # [error  info  warning]，循环severities
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)    # 循环绑定关键字
print("[*] Waiting for logs. To exit press CTRL+C.")

### 定义一个回调函数，用来接收生产者发送的消息 ###
def callback(ch, method, properties, body):
    print("[x] {}: {}".format(method.routing_key, body))

### 订阅消费者 ###
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback)

### 开始消费：循环取消息 ###
channel.start_consuming()