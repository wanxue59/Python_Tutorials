"""
参考文档：Python RabbitMQ RPC实现
参考网址：https://www.cnblogs.com/xiangsikai/p/8304921.html
"""
#_*_coding:utf-8_*_
import pika
import time
# 连接rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# 生成rpc queue
channel.queue_declare(queue='rpc_queue')

#　斐波那契数列
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# 收到消息就调用
# ch 管道内存对象地址
# method 消息发给哪个queue
# props 返回给消费的返回参数
# body数据对象
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)

    response = fib(n)    # 调用斐波那契函数 传入结果

    ch.basic_publish(exchange='',    # 生产端随机生成的queue
                     routing_key=props.reply_to,    # 获取UUID唯一 字符串数值
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))    # 消息返回给生产端

    # 通知MQ这条消息对应处理成功，可以删除这条消息了
    ch.basic_ack(delivery_tag = method.delivery_tag)    # 确保任务完成

# 消费者不止这一个时，谁先处理完谁就去消息队列取，这句话最好在每个消费者端都加上，这儿服务器端同样也加上
channel.basic_qos(prefetch_count=1)

# 监听rpc_queue队列，一收到来自客户端的消息则促发回调on_request
# rpc_queue收到消息:调用on_request回调函数
# queue='rpc_queue'从rpc内收
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()