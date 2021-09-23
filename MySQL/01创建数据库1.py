import pymysql

"""pymysql使用步骤
    核心类 Connect链接用  和Cursor读写用
    1.与数据库服务器建立链接
    2.获取游标对象 (用于发送和接收数据)
    3.用游标执行sql语句
    4.使用fetch方法来获取执行的结果
    5.关闭链接  先关游标 再关链接

    游标的常用方法
    1.创建游标  conn.cursor(指定查询结果的数据类型)
    2.excute  执行sql
    3.fetchone(当sql只有一条记录时)  many(sql有多条并且需要指定条数)  all(多条)
    4.scroll  用于修改游标的当前位置


    注意: pymysql 默认不提交修改  但是注意(指的是对表中记录的操作不提交)  像删库 删表 是无法撤销的


"""


######### 1、打开数据库连接，创建一个数据库对象 #########
db = pymysql.connect(host="localhost", user="testuser",
                     password="testuser123", charset="utf8")    # 打开数据库连接，创建一个数据库对象

######### 2、使用cursor()方法创建一个游标对象 #########
cursor = db.cursor()    # 使用cursor()方法创建一个游标对象

######### 3、使用execute()方法执行SQL创建数据库命令 #########
sql1 = "create database testdb2 character set utf8;"    # 创建名为testdb2数据库
sql2 = "use testdb2;"    # 使用数据库testdb2
sql3 = "create table blogs(id char(20),user_id char(20),name char(20),)character set utf8;"
cursor.execute(sql1)    # 使用execute()方法执行SQL
cursor.execute(sql2)    # 使用execute()方法执行SQL查询
cursor.execute(sql3)    # 使用execute()方法执行SQL查询

######### 4、使用fetchone()方法获取单条数据 #########
data = cursor.fetchone()    # 使用fetchone()方法获取单条数据

print(data)

######### 5、关闭数据库连接 #########
db.close()    # 关闭数据库连接