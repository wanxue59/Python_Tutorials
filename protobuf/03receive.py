import pika
import addressbook_pb2 as pb

### 创建socket ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 声明channel ###
channel = connection.channel()

### 声明queue ###
channel.queue_declare(queue="proto")


### 声明回调函数 ###
def callback(ch, method, properties, body):
    # print(ch, method, properties,body)
    AddressBook = pb.AddressBook()
    AddressBook.ParseFromString(body)
    with open('addressbook.txt', 'a+') as f:
        f.write(AddressBook)
    print("proto文件的内容为:", AddressBook)


### 消费的信息 ###
channel.basic_consume(queue="proto",
                      on_message_callback=callback,
                      auto_ack=True)

### 开启消费 ###
channel.start_consuming()
