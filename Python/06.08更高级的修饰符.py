"""
1. 能够接收任何参数的通用参数装饰器
"""
def checkParams(fn):    # 定义通用参数装饰器函数
    def wrapper(*arg, **kwargs):    # 使用字典和元组的解包参数来作形参
        if isinstance(arg[0], (str)):    # 判断参数是否为字符串类型
            return fn(*arg, **kwargs)    # 若是，则将参数透传给原函数，并返回
        print("variable strname is not a string type")    # 若参数不符合条件，在打印警告
        return
    return wrapper    # 将装饰后的函数返回fun = wrapperfun2("Anna")    # 身份不对，直接返回
"装饰器checkParams变得更加灵活，不仅适用于对wrapper的装饰，同样适用于与wrapper参数不同的函数"

def wrapperfun(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):  # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数

@checkParams    # 使用@修饰符来实现对wrapperfun的修饰，代替wrapperfun2 = checkParams(wrapperfun)
def wrapperfun(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):  # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数

fun = wrapperfun("Anna")    # wrapperfun2为带有参数检查的闭合函数
fun(35)    # 为age赋值，打印输出
fun = wrapperfun(35)    # 当输入参数不合法时，打印警告：variable strname is not a string type
print("-"*100)
print("-"*100)



"""
2. 可接收参数的通用装饰器
"""
def isadmin(userid):    # 可以接收参数的装饰器函数
    def checkParams(fn):  # 定义通用参数装饰器函数
        def wrapper(*arg, **kwargs):  # 使用字典和元组的解包参数来作形参
            if userid != "admin":  # 对外部调用环境进行判断，若不是admin，则直接返回
                print("Operation is prohibited as you are not admin!")  # 若参数不符合条件，在打印警告
                return
            if isinstance(arg[0], (str)):  # 判断参数是否为字符串类型
                return fn(*arg, **kwargs)  # 若是，则将参数透传给原函数，并返回
            print("variable strname is not a string type")  # 若参数不符合条件，在打印警告
            return
        return wrapper  # 将装饰后的函数返回
    return checkParams

@isadmin(userid="admin")    # 在admin模块中，传入admin身份到装饰器
def wrapperfun(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):
        # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数

@isadmin(userid="user")    # 在user模块中，传入user身份到装饰器
def wrapperfun2(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):  # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数

fun = wrapperfun("Anna")    # wrapperfun为带有参数检查的闭合函数
fun(35)    # 为age赋值
fun = wrapperfun2("Anna")    # 身份不对，直接返回



print("-"*100)
print("-"*100)

"""
3. 装饰器返回函数的名称修复
    当函数被装饰完后，对函数的名字属性再赋一次值，将函数的名称恢复过来。这样就可以避免出现装饰完后函数名字变化的现象
"""
"方法一"
def isadmin(userid):    # 可以接收参数的装饰器函数
    def checkParams(fn):  # 定义通用参数装饰器函数
        def wrapper(*arg, **kwargs):  # 使用字典和元组的解包参数来作形参
            if userid != "admin":  # 对外部调用环境进行判断，若不是admin，则直接返回
                print("Operation is prohibited as you are not admin!")  # 若参数不符合条件，在打印警告
                return
            if isinstance(arg[0], (str)):  # 判断参数是否为字符串类型
                return fn(*arg, **kwargs)  # 若是，则将参数透传给原函数，并返回
            print("variable strname is not a string type")  # 若参数不符合条件，在打印警告
            return
        wrapper.__name__ = fn.__name__    # 将函数名称属性恢复
        return wrapper  # 将装饰后的函数返回
    return checkParams
# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------
"方法二"
import functools
def isadmin(userid):    # 可以接收参数的装饰器函数
    def checkParams(fn):  # 定义通用参数装饰器函数
        @functools.wraps(fn)    # 内置的装饰器，用于恢复函数名称
        def wrapper(*arg, **kwargs):  # 使用字典和元组的解包参数来作形参
            if userid != "admin":  # 对外部调用环境进行判断，若不是admin，则直接返回
                print("Operation is prohibited as you are not admin!")  # 若参数不符合条件，在打印警告
                return
            if isinstance(arg[0], (str)):  # 判断参数是否为字符串类型
                return fn(*arg, **kwargs)  # 若是，则将参数透传给原函数，并返回
            print("variable strname is not a string type")  # 若参数不符合条件，在打印警告
            return
        wrapper.__name__ = fn.__name__    # 将函数名称属性恢复
        return wrapper  # 将装饰后的函数返回
    return checkParams