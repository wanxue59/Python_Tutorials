"""
class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[],
                             formatter_class=argparse.HelpFormatter, prefix_chars='-',
                             fromfile_prefix_chars=None, argument_default=None,
                             conflict_handler='error', add_help=True, allow_abbrev=True,
                             exit_on_error=True)
创建新对象时，所有参数都会作为关键字被传入(sys.argv:传递给Python脚本的命令行参数列表)：

    prog - 程序的名称（默认：sys.argv[0]）
    usage - 描述程序用途的字符串（默认值：从添加到解析器的参数生成，在用法消息中可以使用 %(prog)s格
式说明符来填入程序名称。）
    description - 在参数帮助文档之前显示的文本（默认值：无）
    epilog - 在参数帮助文档之后显示的文本（默认值：无）
    parents - 一个 ArgumentParser 对象的列表，它们的参数也应包含在内
    formatter_class - 用于自定义帮助文档输出格式的类
    prefix_chars - 可选参数的前缀字符集合（默认值：’-’）
    fromfile_prefix_chars - 当需要从文件中读取其他参数时，用于标识文件名的前缀字符集合（默认值：None）
    argument_default - 参数的全局默认值（默认值： None）
    conflict_handler - 解决冲突选项的策略（通常是不必要的）
    add_help - 为解析器添加一个 -h/–help 选项（默认值： True）
    allow_abbrev - 如果缩写是无歧义的，则允许缩写长选项 （默认值：True）
    exit_on_error - 决定当错误发生时是否让 ArgumentParser 附带错误信息退出。 (默认值: True)

原文链接：https://blog.csdn.net/qq_41214679/article/details/112875235

"""
import argparse

# 第一步:创建一个ArgumentParser对象;ArgumentParser 对象包含将命令行解析成 Python 数据类型所需的全部信息。
parser = argparse.ArgumentParser(description='Process some integers.')

# 第二步：添加参数；通过调用 add_argument() 方法完成的。这些信息在 parse_args() 调用时被存储和使用。
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# 第三步：解析参数；parse_args()方法解析参数。在脚本中，通常parse_args()会被不带参数调用，
# 而ArgumentParser将自动从sys.argv中确定命令行参数。
args = parser.parse_args()

print(args.accumulate(args.integers))
