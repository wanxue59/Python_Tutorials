"""
10.4.2  实例37：使用协程实现“任务提交”与“结果接收”
封装及回调协程的任务
    在得到协程对象与事件循环对象后，有两种创建任务的方式：
    （1）使用事件循环对象的create_task方法
    （2）使用asyncio模块下的ensure_future函数
    得到任务对象后，就可以调用该任务对象的add_done_callback方法来实现回调函数的绑定。等任务执行完后，系统
会自动将任务的结果传入回调函数中的future参数，通过future的result方法即可得到结果
实例描述：
    使用协程机制处理一个任务。要求：提交任务时传入任务参数，任务结束后获得执行结果。
"""
import asyncio

async def do_some_work(x):    # 定义协程处理函数
    print("任务：", x)
    return "任务：{}的返回结果".format(x)

def callback(future):    # 回调函数
    print("Callback: ", future.result())    # 返回任务结果

coroutine = do_some_work("爬取当天股票")    # 定义协程并传入任务
loop = asyncio.get_event_loop()    # 获取事件循环对象
task = asyncio.ensure_future(coroutine)    # 获得任务对象（对协程的封装）
task.add_done_callback(callback)    # 封装好后的协程对象（任务）就可以绑定回调函数了
loop.run_until_complete(task)    # 执行协程任务
"""
输出结果：
    任务： 爬取当天股票
    Callback:  任务：爬取当天股票的返回结果
第一行的显示，表明接到了处理任务；第二行的显示，表明收到了任务处理后的结果
"""