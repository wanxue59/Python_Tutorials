import pika
import sys
### 建立socket ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 创建channel ###
channel = connection.channel()

### 定义direct类型的exchange ###
# 不指定queue的名字，rabbit会随机分配一个名字，exclusive=True会在使用此queue的消费者断开后，自动将queue删除，result是queue的对象
channel.exchange_declare(exchange='direct_logs',exchange_type='direct')
result = channel.queue_declare(queue='',    # 不指定具体的名字
                               exclusive=True)
queue_name = result.method.queue    # 获取queue名

### 手动输入安全级别 ###
severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n"%sys.argv[0])
    sys.exit(1)
### 循环遍历绑定消息队列 ###
for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
print("[*] Waiting for logs. To exit press CTRL+C")

### 声明回调函数 ###
def callback(ch, method, properties, body):
    print("[x] %r %r" %method.routing, body)

### 消费信息 ###
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

### 开启消费 ###
channel.start_consuming()