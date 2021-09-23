"""删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据"""
import pymysql

# 打开数据库连接，创建一个数据库对象
db = pymysql.connect(host="localhost", user="testuser", password="testuser123", database="testdb")

cursor = db.cursor()    # 使用cursor()方法创建一个游标对象

# SQL删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s"%(20)    # 将年龄大于20的数据删除

try:
    cursor.execute(sql)    # 执行sql语句
    db.commit()    # 提交到数据库执行
except:
    db.rollback()    # 发生错误时回滚

db.close()    # 关闭数据库