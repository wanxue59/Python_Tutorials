'''生产者'''
import pika
# 通过这个实例创建连接connection到localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 声明一个channel
channel = connection.channel()
# 声明队列queue
channel.queue_declare(queue='hello')    # queue名为hello
# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
channel.basic_publish(exchange='',
                      routing_key='hello',    # queue的名字
                      body='Hello World!')    # 具体的消息内容
print("[x] Sent 'Hello World!'")
connection.close()    # 直接关闭连接