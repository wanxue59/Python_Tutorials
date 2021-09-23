
import pika

### 指定远程 rabbitmq 的用户名密码并创建凭证 ###
# credentials = pika.PlainCredentials(username='host0720', password='111111')

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
# connection = pika.BlockingConnection(pika.ConnectionParameters( host='127.0.0.1', port=5672, virtual_host='host0720', credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 声明队列queue，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行 ###
channel.queue_declare(queue="nulige", durable=True)    # 队列持久化

### 将消息发送到RabbitMQ并持久化 ###
channel.basic_publish(exchange='',
                      routing_key='nulige',    # send msg to this queue
                      body="Hello World!23",
                      properties=pika.BasicProperties(delivery_mode=2))    # 消息持久化
print("[x] Sent 'Hello World!23'")

### 关闭与rabbit的连接 ###
connection.close()