"""消费者"""
import pika
### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
### 创建一个AMQP信道（channel） ###
channel = connection.channel()
### 声明队列queue ###
channel.queue_declare(queue='hello')    # queue名为hello
### 定义回调处理消息的函数 ###
def callback(ch, method, properties, body):
    print("[x] Received %r."%body)
    print("callback各参数意义：")    # ch:channel的实例；method：一些参数；properties：属性
    print("ch:{};\nmethod:{};\nproperties:{}\n".format(ch, method, properties))
### 消费者消费：告诉rabbitmq，用callback来接收并处理消息 ###
channel.basic_consume(queue='hello',
                      on_message_callback=callback,  # 获取body后执行回调函数
                      auto_ack=True)    # 自动应答开启，会给MQ服务器发送一个ack：“已经收到了”
print("[*] Waiting for messages. To eixt press CTAL+C")
channel.start_consuming()    # 启动消费模式