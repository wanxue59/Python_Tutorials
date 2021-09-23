import pika
import json
### 将数据转成json格式
data = 'Hello World!'
data2 = json.dumps(data)

### 连接rabbitmq服务器 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 声明channel ###
channel = connection.channel()

### 声明queue ###
channel.queue_declare(queue='JSON')

### 通过一个空的exchange发送内容至queue ###
channel.basic_publish(exchange='',
                      routing_key='JSON',    # queue的名字
                      body=data2)    # 要发送的消息

### 关闭连接 ###
connection.close()    # 直接关闭连接