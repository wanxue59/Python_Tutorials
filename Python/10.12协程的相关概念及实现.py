"""
10.4.1  协程的相关概念及实现
在Python中，能够实现协程的模块有多个，如asyncio, tornado 或 gevent
以asyncio为例，介绍创建协程用到的相关概念
    event_loop（事件循环）：是一个协程处理函数的调用机制。程序会开启有一个无限循环，当事件发生时，调用相应
的协程函数
    coroutine（协程对象）：指一个使用async关键字来定义的函数。调用该函数，会返回一个协程对象。该协程对象就
是一个处于挂起状态的协程函数，需要注册到事件循环event_loop进行调用
    task任务：是对协程的进一步封装
    future：等同于task，代表执行任务的结果
    async/await关键字：async用于定义一个协程，await用于挂起阻塞的异步调用接口
"""
import asyncio

async def do_some_work(x):    # 定义协程处理函数
    print(x)
coroutine = do_some_work("hello")    # 生成协程对象，并传入"hello"
loop = asyncio.get_event_loop()    # 获得事件循环对象
try:
    loop.run_until_complete(coroutine)    # 将协程注册到实现事件循环对象中，并开始运行
finally:
    loop.close()    # 程序结束关闭事件循环对象