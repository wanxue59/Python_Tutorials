"""
    装饰器的主要作用就是在扩展原有功能的基础上，最大化地使用已有代码。也可以理解成：在不改变原有代码实现的基础上，添加新的实现功能。
    装饰器的实现方法是：在原有的函数外面再包装一层函数，使新函数在返回原有函数之前实现一些其他的功能。
"""
def checkParams(fn):    # 装饰器函数，参数是要被装饰的函数。相当于闭合函数
    def wrapper(strname):    # 添加新的实现功能：定义一个检查参数的函数
        if isinstance(strname, (str)):    # 判断参数是否为字符串类型
            return fn(strname)    # 若是，则调用fn(strname)返回计算结果
        print("variable strname is not a string type")    # 若参数不符合条件，在打印警告
        return
    return wrapper    # 将装饰后的函数返回

def wrapperfun(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):  # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数

wrapperfun2 = checkParams(wrapperfun)    # 对wrapperfun进行修饰，即，将自由变量谁wrapperfun函数
fun = wrapperfun2("Anna")    # wrapperfun2为带有参数检查的闭合函数
fun(35)    # 为age赋值，打印输出
fun = wrapperfun2(35)    # 当输入参数不合法时，打印警告：variable strname is not a string type


"使用修饰符实现上述功能"
"""
    修饰符的作用是，在定义原函数时就可以为其指定修饰器函数。
    这样做的好处是：使修饰器与被修饰函数的关系更加明显，也使得需要修饰的函数在第一时间得到修饰，降低了编码出错的可能性。
    @修饰符的语法是：在@后面添加修饰器函数，同时在其下一行添加被修饰函数的定义
"""
print("使用@修饰符实现上述功能：")
@checkParams    # 使用@修饰符来实现对wrapperfun的修饰，代替wrapperfun2 = checkParams(wrapperfun)
def wrapperfun(strname):    # 闭合函数，strname作为自由变量
    def recoder(age):  # 定义一个嵌套函数recorder
        print("姓名：", strname, "年龄：", age)
    return recoder    # 返回recorder函数

fun = wrapperfun("Anna")    # wrapperfun2为带有参数检查的闭合函数
fun(35)    # 为age赋值，打印输出
fun = wrapperfun(35)    # 当输入参数不合法时，打印警告：variable strname is not a string type