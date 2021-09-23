import pika
import addressbook_pb2 as pb

### 对pb文件中的变量进行赋值 ###
AddressBook = pb.AddressBook()
person = AddressBook.people.add()
person.id = 1
person.name = "RRN"
person.email = "ranrn@qq.com"
phone_number = person.phones.add()
phone_number.number = "13244556677"
phone_number.type = pb.MOBILE



### 建立socket ###
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

### 声明channel ###
channel = connection.channel()

### 声明queue ###
channel.queue_declare(queue='proto')

### 通过一个空的exchange发送内容至queue ###

### 序列化 ###
# print(AddressBook)
data = AddressBook.SerializeToString()
print(AddressBook.ParseFromString(data))
channel.basic_publish(exchange="",
                  routing_key="proto",
                  body=data)


### 关闭连接 ###
connection.close()