"""
topic--消费者
"""
import pika
import sys

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


result = channel.queue_declare(queue='', exclusive=True)    # 排他性，唯一性
queue_name = result.method.queue


binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n"%sys.argv[0])
    sys.exit(1)

### 将队列和交换器绑定 ###
for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)
print("[x] Waiting for logs. To exit press CTRL+C.")

### 定义一个回调函数，用来接收生产者发送的消息 ###
def callback(ch, method, properties, body):
    print("[x] {}: {}".format(method.routing_key, body))

### 订阅消费者 ###
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

### 开始消费：循环取消息 ###
channel.start_consuming()