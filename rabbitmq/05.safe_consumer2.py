"""生产者：auto=False（自动应答关闭）"""
import pika
import time
### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
### 创建一个AMQP信道（channel） ###
channel = connection.channel()
### 声明队列queue ###
channel.queue_declare(queue='task_queue')    # queue名为task_queue

### 定义回调处理消息的函数 ###
def callback(ch, method, properties, body):
    print("[x] Received %r."%body)    # body为二进制格式
    # time.sleep(20)
    print("[x] Done")
    print("method.delivery_tag", method.delivery_tag)
    print("properties", properties)
    ch.basic_ack(delivery_tag=method.delivery_tag)    # 消费者收到消息返回消息标识符（ack：acknowledge）

### 消费者消费：告诉rabbitmq，用callback来接收并处理消息 ###
channel.basic_consume(queue='task_queue',
                      on_message_callback=callback,  # 获取body后执行回调函数
                      auto_ack=False)  # 自动应答关闭，消息不需要确认（与no_ack一样，只是叫法不一样）
print("[*] Waiting for messages. To eixt press CTAL+C")
channel.start_consuming()    # 启动消费模式