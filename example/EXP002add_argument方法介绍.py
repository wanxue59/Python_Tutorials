"""
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type]
                            [, choices][, required][, help][, metavar][, dest])
定义单个的命令行参数的具体解析，参数如下：

    name or flags - 一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
    action - 当参数在命令行中出现时使用的动作基本类型。
    nargs - 命令行参数应当消耗的数目。
    const - 被一些 action 和 nargs 选择所需求的常数。
    default - 当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
    type - 命令行参数应当被转换成的类型。
    choices - 可用的参数的容器。
    required - 此命令行选项是否可省略 （仅选项可用）。
    help - 一个此选项作用的简单描述。
    metavar - 在使用方法消息中使用的参数值示例。
    dest - 被添加到 parse_args() 所返回对象上的属性名。

name or flags
    add_argument() 方法必须知道它是否是一个选项，例如 -f 或 --foo，或是一个位置参数，例如一组文件名。第一个
传递给 add_argument() 的参数必须是一系列 flags 或者是一个简单的参数名。
    当 parse_args() 被调用，选项会以 - 前缀识别，剩下的参数则会被假定为位置参数:

原文链接：https://blog.csdn.net/qq_41214679/article/details/112875235

"""
import argparse

parser = argparse.ArgumentParser(description="add_argument传参示例")

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store',
                    help='Store a constant value')

parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch',
                    help='Set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean_switch',
                    help='Set a switch to false')

parser.add_argument('-a', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list')

parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append',
                    default=[],
                    help='Add different values to list')
parser.add_argument('-B', action='append_const', dest='const_collection',
                    const='value-2-to-append',
                    help='Add different values to list')

parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-v', '--variable', default='666', dest='variable', help='随便举例')

results = parser.parse_args()


print('simple_value  =   ', results.simple_value)
print('constant_value  =  ', results.constant_value)
print('boolean_switch  =   ', results.boolean_switch)
print('collection  =  ', results.collection)
print('const_collection  =  ', results.const_collection)
print('variable  =  ', results.variable)

