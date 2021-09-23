import pymysql

# 打开数据库连接，创建一个数据库对象
db = pymysql.connect(host="localhost", user="testuser", password="testuser123", database="testdb")    # 打开数据库连接，创建一个数据库对象

cursor = db.cursor()    # 使用cursor()方法创建一个游标对象
money = 30000

# SQL插入语句
sql = """INSERT INTO EMPLOYEE (FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Joney', 'mee', 20, 'F', money)"""

try:
    cursor.execute(sql)    # 执行sql语句
    db.commit()    # 提交到数据库执行
except:
    db.rollback()    # 如果发生错误则回滚

db.close()    # 关闭数据库连接