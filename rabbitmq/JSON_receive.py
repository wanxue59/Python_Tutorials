import pika
# import json
### 连接rabbitmq服务器 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 创建channel ###
channel = connection.channel()

### 声明queue ###
channel.queue_declare(queue='JSON')

### 声明回调函数callback ###
def callback(ch, method, properties, body):
    print("JSON文件内容为：{0}".format(body))

### 消费的消息 ###
channel.basic_consume(queue='JSON',
                      on_message_callback=callback,
                      auto_ack=True)
### 开启消费 ###
channel.start_consuming()