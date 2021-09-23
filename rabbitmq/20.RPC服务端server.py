"""
参考文档：python实现RabbitMQ六种模式
参考网址：https://blog.csdn.net/qq_37623764/article/details/105767004
"""
import pika
import uuid    # 用于生成请求的唯一标识correlation_id

class RpcClient(object):
    def __init__(self):
        '''初始化时就建立channel，接收服务端的任务结果'''
        # 连接rabbitmq服务器
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        # 创建随机回调队列，用于告诉服务端，任务的结果放在这个随机队列中
        result = self.channel.queue_declare(queue='', exclusive=True)

        self.callback_queue = result.method.queue    # 拿到这个随机队列名

        # 监听这个回调队列，一旦有响应结果就促发回调on_response(就是为了对比id)
        self.channel.basic_consume(queue=self.callback_queue,
                                   auto_ack=True,
                                   on_message_callback=self.on_response)



    # 对比id确定这个结果确实是我的响应结果
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())    # 用于生成请求的唯一标识
        # 向rpc_queue队列中塞消息body,并添加reply_to和correlation_id两个属性
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                                                   ),
                                   body=str(n)# 消息
                                   )

        while self.response is None:
            # 防止连接自动断开,消费者主线程定时发心跳交互,耗时较长的消息消费
            self.connection.process_data_events()
        return str(self.response)


rpc = RpcClient()
response = rpc.call(8)
print("客户端已发出RPC请求，我客户端这边传了个2给你，想要调用你服务器端的fit函数")
print("客户端拿到本次RPC请求的响应结果:{}".format(response))
