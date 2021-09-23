"""
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据
·fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
·fetchall(): 接收全部的返回结果行
·rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数
"""
import pymysql

# 打开数据库连接，创建一个数据库对象
db = pymysql.connect(host="localhost", user="testuser", password="testuser123", database="testdb")

cursor = db.cursor()    # 使用cursor()方法创建一个游标对象

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s"%(1000)    # SQL查询语句
                                                           # 从表EMPLOYEE中查找所有INCOME>1000的数据

try:
    cursor.execute(sql)    # 执行SQL语句
    results = cursor.fetchall()    # 获取所有记录列表
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("FIRST_NAME: {},  LAST_NAME: {},  AGE: {}, SEX: {},  INCOME: {}.".format(
            fname, lname, age, sex, income))    # 打印结果
except:
    print("Error: unable to fetch data")

db.close()    # 关闭数据库