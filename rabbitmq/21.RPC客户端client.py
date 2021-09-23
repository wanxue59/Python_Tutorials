"""
参考文档：python实现RabbitMQ六种模式
参考网址：https://blog.csdn.net/qq_37623764/article/details/105767004
"""
import pika

# 连接rabbitmq服务器
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='x.x.x.x'))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建rpc_queue队列
channel.queue_declare(queue='rpc_queue')


def fun(n):
    return 100 * n

# body就是来自客户端塞进队列的消息，props就是来自客户端properties里的两个键值对
# ch: 消息发给哪个queue  method: 管道内存对象地址  props: 返回给客户端client的返回参数  body: 数据对象
def on_request(ch, method, props, body):
    n = int(body)
    response = fun(n)
    # 向接收到的props.reply_to队列塞进响应结果response
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    print("服务器端已经把响应结果放进客户端的回调队列了，结果是:{}".format(response))

    # 通知MQ这条消息对应处理成功，可以删除这条消息了
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 消费者不止这一个时，谁先处理完谁就去消息队列取，这句话最好在每个消费者端都加上，这儿服务器端同样也加上
channel.basic_qos(prefetch_count=1)

# 监听rpc_queue队列，一收到来自客户端的消息则促发回调on_request
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print("服务器端正在等待客户端往rpc_queue放消息......")

channel.start_consuming()
