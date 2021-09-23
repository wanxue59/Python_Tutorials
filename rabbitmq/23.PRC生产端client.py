"""
参考文档：Python RabbitMQ RPC实现
参考网址：https://www.cnblogs.com/xiangsikai/p/8304921.html
"""
import pika
import uuid
import time

# 斐波那契数列 前两个数相加依次排列
class FibonacciRpcClient(object):
    def __init__(self):
        # 链接远程
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)    # 生成随机queue
        self.callback_queue = result.method.queue    # 拿到随机队列名，发给消费端

        # 监听这个回调队列，一旦有响应结果就促发回调on_response(就是为了对比id)
        # self.on_response 回调函数:只要收到消息就调用这个函数。
        # 声明收到消息后就 收queue=self.callback_queue内的消息
        self.channel.basic_consume(queue=self.callback_queue,
                                   auto_ack=True,
                                   on_message_callback = self.on_response)

    # 收到消息就调用  对比id确定这个结果确实是我的响应结果
    # ch 管道内存对象地址
    # method 消息发给哪个queue
    # body数据对象
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:    # 判断本机生成的ID 与 生产端发过来的ID是否相等
            self.response = body    # 将body值 赋值给self.response


    def call(self, n):
        self.response = None    # 赋值变量，一个循环值

        self.corr_id = str(uuid.uuid4())    #　随机生成一个唯一的字符串

        # routing_key='rpc_queue' 发一个消息到rpc_queue内
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(

                                         # 执行命令之后结果返回给self.callaback_queue这个队列中
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,    # 生成UUID 发送给消费端
                                         ),
                                   body=str(n))    # 发的消息，必须传入字符串，不能传数字

        # 没有数据就循环收
        while self.response is None:
            # 非阻塞版的start_consuming()
            # 没有消息不阻塞
            self.connection.process_data_events()
            print("no msg...")
            time.sleep(0.5)
        return int(self.response)

#　实例化
fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(6)
print(" [.] Got %r" % response)