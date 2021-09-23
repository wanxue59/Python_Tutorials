import pika
import time

### 指定远程 rabbitmq 的用户名密码并创建凭证 ###
# credentials = pika.PlainCredentials(username="host0720", password="111111")

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
# connection = pika.BlockingConnection(pika.ConnectionParameters(host="http://localhost:15672/", credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
### 创建一个AMQP信道（channel） ###
channel = connection.channel()

### 声明队列queue，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行 ###
channel.queue_declare(queue="nulige", durable=True)    # 队列持久化

### 定义一个回调函数，用来接收生产者发送的消息 ###
def callback(ch, method, properties, body):
    print("\tch: {};\n\tmethod: {};\n\tproperties: {}".format(ch, method, properties))
    print("[x] Received %r"%body)
    time.sleep(1)

### 订阅消费者 ###
channel.basic_consume(queue="nulige",
                      on_message_callback=callback)
channel.basic_qos(prefetch_count=1)    # 在消费者端，配置perfetch=1,表明消费者当前消息还没处理，不要再发新消息
print("[*]  Waiting for messages. To exit press CTRL+C.")

### 开始消费：循环取消息 ###
channel.start_consuming()    # 启动消费模式