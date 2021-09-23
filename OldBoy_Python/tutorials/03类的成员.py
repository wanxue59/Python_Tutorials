# -*- coding: utf-8 -*-
"""
参考文档：python 面向对象（进阶篇）
网址：https://www.cnblogs.com/wupeiqi/p/4766801.html
Project: Tutorials
File Name: 03类的成员
Author: wjz
date: 2021-09-15
"""
"""
类成员：字段；方法；属性
一、字段的定义和使用
字段：普通字段、静态字段
     普通字段：属于对象，在每个对象中都保存一份，只有对象能够使用
     静态字段：属于类，只在类中保存一份，类和对象都可以使用
注：所有成员中，只有普通字段的内容保存对象中，即：根据此类创建了多少对象，在内存中就有多少个普通字段。而其他的成员，则都是保存在类中，
   即：无论对象的多少，在内存中只创建一份。
应用场景：通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段

二、方法的定义和使用
方法：普通方法，类方法，静态方法
     普通方法：由对象调用，至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self
     类方法：由类调用，至少一个cls参数；执行类方法时，自动将调用该类方法的类复制给cls
     静态方法：由类调用，无默认参数
相同点：对于所有方法而已，均属于类（非对象）中，所有，在内存中只保存一份
不同点：方法调用者不同，调用方法时自动传入的参数不同

三、属性
定义：
    方法一：装饰器--在普通方法的基础上添加@property装饰器；属性仅有一个self参数
    方法二：静态字段--在类中定义值为property对象的静态字段
调用：方法调用时必须带括号；属性调用时括号可带可不带
功能：属性内部进行一系列的逻辑计算，最终将计算结果返回
"""

"""
一、字段的定义和使用
字段：普通字段、静态字段
     普通字段：属于对象，在每个对象中都保存一份，只有对象能够使用
     静态字段：属于类，只在类中保存一份，类和对象都可以使用
注：所有成员中，只有普通字段的内容保存对象中，即：根据此类创建了多少对象，在内存中就有多少个普通字段。而其他的成员，则都是保存在类中，
   即：无论对象的多少，在内存中只创建一份。
应用场景：通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段
"""
class Province:
    # 静态字段：属于类，类和对象都可以使用
    country = "中国"

    def __init__(self, name):
        # 普通字段：属于对象，只有对象能够使用
        self.name = name


print("***"*20)
print("不实例化，直接访问静态字段：", Province.country)
print("---"*10)

obj = Province("湖北省")
# 访问静态字段
print("访问静态字段",)
print("\t直接访问静态字段：", Province.country)    # 直接访问静态字段
print("\t利用类来访问静态字段：", obj.country)    # 利用对象访问静态字段
print("---"*10)
# 访问普通字段
print("访问普通字段：")
print("\t利用对象直接访问普通字段：", obj.name)
# print("用类访问普通字段，会报错：", Province.name)
print("***"*20)
print("\n")

# ************************************************************************************************************ #

"""
二、方法的定义和使用
方法：普通方法，类方法，静态方法
     普通方法：由对象调用，至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self
     类方法：由类调用，至少一个cls参数；执行类方法时，自动将调用该类方法的类复制给cls
     静态方法：由类调用，无默认参数
相同点：对于所有方法而已，均属于类（非对象）中，所有，在内存中只保存一份
不同点：方法调用者不同，调用方法时自动传入的参数不同
"""

class Foo:
    def __init__(self, name):
        self.name = name

    # 定义普通方法，至少有一个self参数
    def ord_func(self):
        return "普通方法"

    # 定义类方法，至少有一个cls参数
    @classmethod
    def cls_func(cls):
        return "类方法"

    # 定义静态方法，无默认参数
    @staticmethod
    def sta_func():
        return "静态方法"


print("***"*20)
print("不实例化对象，直接用类调用方法：")
# print("不实例化对象，直接用类调用普通方法，会报错：", Foo.ord_func())
print("\t用类调用类方法：", Foo.cls_func())
print("\t用类调用静态方法：", Foo.sta_func())
print("---"*10)    # 分割线

print("实例化对象后，再调用方法：")
fo = Foo("方法")    # 创建对象fo
# print("\t用类调用普通方法，会报错：", Foo.ord_func())    # 用类调用普通方法，会报错
print("\t用对象调用普通方法：", fo.ord_func())    # 用对象调用普通方法
print("\t用类调用类方法：", Foo.cls_func())    # 用类调用类方法
print("\t用对象调用类方法：", fo.cls_func())    # 用对象调用类方法
print("\t用类调用静态方法：", Foo.sta_func())
print("\t用对象调用静态方法：", fo.sta_func())
print("***"*20)
print("\n")

# ************************************************************************************************************ #

"""
三、属性
定义：
    方法一：装饰器--在普通方法的基础上添加@property装饰器；属性仅有一个self参数
    方法二：静态字段--在类中定义值为property对象的静态字段
调用：方法调用时必须带括号；属性调用时括号可带可不带
功能：属性内部进行一系列的逻辑计算，最终将计算结果返回
"""

# 一、属性的基本使用
class Property1:
    def func(self):
        print("方法")

    # 定义属性
    @property
    def prop(self):
        print("属性")


# 属性的调用
print("***"*20)
pro1 = Property1()    # 创建对象pro
pro1.func()    # 调用方法
pro1.prop   # 调用对象
print("---"*10)
# -------------------------------------------------------------- #

# 二、装饰器定义属性
# 经典类
class Property2:
    @property
    def price(self):
        return "经典类中定义属性"

pro2 = Property2()
print("装饰器定义属性：", pro2.price)
print("---"*10)


# 新式类
class Property3(object):
    @property
    def price(self):
        return "@property"

    @price.setter
    def price(self, value):
        return "@price.setter"

    @price.deleter
    def price(self):
        return "@price.deleter"

pro3 = Property3()
print(pro3.price)
pro3.price = 123
print(pro3.price)
print("---"*10)


# 由于新式类中具有三种访问方式，我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
class Goods1(object):
    def __init__(self):
        self.original_price = 100    # 原价
        self.discount = 0.8    # 折扣

    @property
    def price(self):
        new_price = self.original_price * self.discount    # 实际价格 = 原价 * 折扣
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self, value):
        del self.original_price

goods1 = Goods1()
print("商品价格为：", goods1.price)    # 获取商品价格
goods1.price = 200    # 修改商品原价
print("修改后商品价格为：", goods1.price)
del goods1.original_price    # 删除商品原价
print("---"*10)
# -------------------------------------------------------------- #

# 三、静态字段定义属性
"当使用静态字段的方式创建属性时，经典类和新式类无区别"
class Property4:
    def get_bar(self):
        return "egon"

    BAR = property(get_bar)
pro4 = Property4()
print("返回静态字段方式定义的属性：", pro4.BAR)
print("---"*10)


"""
property的构造方法中有个四个参数：
    ·第一个参数是方法名，调用 对象.属性 时自动触发执行方法
    ·第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
    ·第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
    ·第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
"""
class Property5:
    def get_bar(self):
        return "egon"

    # 必须两个参数
    def set_bar(self, value):
         return 'set value' + value

    def del_bar(self):
        return "egon"

    BAR = property(get_bar, set_bar, del_bar, 'description')
pro5 = Property5()
print("get_bar: ", pro5.BAR)    # 自动调用第一个参数中定义的方法：get_bar
pro5.BAR = "alex"    # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
del pro5.BAR    # 自动调用第三个参数中定义的方法：del_bar方法
pro5.BAR.__doc__    # 自动获取第四个参数中设置的值：description...
print("---"*10)


"由于静态字段方式创建属性具有三种访问方式，我们可以根据他们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除"
class Goods2:
    def __init__(self):
        self.original_price = 100    # 原价
        self.discount = 0.8    # 折扣

    def get_price(self):
        new_price = self.original_price * self.discount    # 实际价格 = 原价 * 折扣
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, "价格属性描述")
goods2 = Goods2()
goods2 = Goods2()
print("商品价格为：", goods2.PRICE)    # 获取商品价格
goods2.PRICE = 200    # 修改商品原价
print("修改后商品价格为：", goods2.PRICE)
del goods2.PRICE    # 删除商品原价
print("---"*10)