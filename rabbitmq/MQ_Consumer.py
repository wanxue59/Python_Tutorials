'''消费者'''
import pika
### 设置connection, channel, queue ###
# 连接rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# 创建一个channel
channel = connection.channel()
channel.queue_declare(queue='hello')    # 再次声明queue，如果队列存在则选择hello队列；否则，创建新队列

### 设置回调函数，也就是收到消息以后做什么 ###
def callback(ch, method, properties,  body):
    '''

    :param ch: send端channel的内存对象的地址
    :param method: 指的send端发给谁，发给哪个Q的一些信息，一般不怎么用
    :param properites: send端的属性，这里指的send端发过来给receive端的属性
    :param body: send端发过来的消息
    :return: None
    '''
    print("--> ch",ch, "method:",method, "properties",properties)
    print('[x] Received %r' %body)

### 设置消费者 ###
channel.basic_consume(# 消费的信息
                      on_message_callback=callback,    # 如果收到消息，就调用callback函数来处理消息
                      queue='hello',    # queue的名字
                      auto_ack=True)    # 消费者收到消息后，给RabbitMQ一个“已收到”的反馈
print("[*] Waiting for messages. To exit press CTRL+C")
# 这个start只要一启动就一直运行，它不止收一条，而是永远收下去，没有消息就在这边卡住
channel.start_consuming()
