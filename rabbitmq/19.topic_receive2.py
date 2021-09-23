"""
参考文档：python实现RabbitMQ六种模式 --  by The_shy等风来
网址：https://blog.csdn.net/qq_37623764/article/details/105767004
topic--消费者
接消息时也要指定关键字，如：
python 18.topic_receive.py error
"""
import pika

### 创建socket：获取与rabbitmq服务的连接，虚拟队列需要指定参数 ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 在 connection 上创建一个AMQP信道（channel） ###
channel = connection.channel()

### 在 channel 上声明交换器 exchange ###
channel.exchange_declare(exchange='topic_logs2', exchange_type='topic')

### 创建一个随机队列 ###
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

### 将队列和交换器绑定 ###
channel.queue_bind(exchange='topic_logs2',
                   queue=queue_name,
                   routing_key='yue.*.#')    # 以routing_key作为关键字
print("[x] Waiting for logs. To exit press CTRL+C.")


def callback(ch, method, properties, body):
    body = body.decode('utf8')
    print("[*] Received {} successfully......".format(body))
    # 给mq发送应答信号，表明数据已经处理完成，可以删除
    ch.basic_ack(delivery_tag=method.delivery_tag)

### 监听随机队列，一旦有值出现，则触发回调函数：callback ###
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback)

### 开始消费：循环取消息 ###
channel.basic_qos(prefetch_count=1)    # 在消费者端，配置perfetch=1,表明消费者当前消息还没处理，不要再发新消息
channel.start_consuming()
