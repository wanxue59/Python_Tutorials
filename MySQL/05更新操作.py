"""更新操作用于更新数据表的数据，以下实例将 TESTDB 表中 SEX 为 'M' 的 AGE 字段递增 1"""
import pymysql

# 打开数据库连接，创建一个数据库对象
db = pymysql.connect(host="localhost", user="testuser", password="testuser123", database="testdb")

cursor = db.cursor()    # 使用cursor()方法创建一个游标对象

# 年龄加一并更新数据库
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 3 WHERE SEX = '%c'"%('M')    # SQL更新语句
sql = "UPDATE EMPLOYEE SET INCOME = INCOME + 5000 WHERE SEX = %s"    # SQL更新语句


try:
    # cursor.execute(sql)  # 执行sql语句
    cursor.execute(sql, ('M', ))  # 执行sql语句
    db.commit()    # 提交到数据库执行
except:
    db.rollback()    # 回滚  就是返回上一步操作的结果

db.close()    # 关闭数据库