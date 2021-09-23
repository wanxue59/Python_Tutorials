import pymysql

# 打开数据库连接，创建一个数据库对象
db = pymysql.connect(host="localhost", user="testuser", password="testuser123", database="testdb")

cursor = db.cursor()    # 使用cursor()方法创建一个游标对象

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")    # 使用execute()方法执行SQL，如果表存在则删除

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)
         time datetime_interval_precision 
         """

cursor.execute(sql)    # 使用execute()方法执行sql语句

db.close()    # 关闭数据库连接