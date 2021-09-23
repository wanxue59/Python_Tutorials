'''Direct广播模式：队列绑定关键字，发送者根据关键字将数据发送到消息exchange，exchange根据关键字判定应该将数据发送至指定队列'''
import pika
import sys
### 建立socket ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 声明channel ###
channel = connection.channel()

### 定义direct类型的exchange ###
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

### 定义重要程度，定义什么级别的日志 ###
severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = ' '.join(sys.argv[2:]) or "Hello World!"

### 发送消息 ###
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

### 关闭连接 ###
connection.close()

