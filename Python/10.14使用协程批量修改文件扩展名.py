"""
10.6  实例38：使用协程批量修改文件扩展名
实例描述：
    在本地D盘中新建一个文件夹test，并在其中放置若干Python代码文件。使用协程批量将这些文件全部转化为扩展名
为“txt”的文件
"""
import asyncio
import os

async def change_files(task, path):    # 协程处理函数
    files = os.listdir(path)    # 列出当前目录下所有的文件

    for filename in files:
        portion = os.path.splitext(filename)    # 分离文件名和后缀
        print("后缀名：", portion)

        if portion[1] == ".py":    # 根据后缀名来修改，如无后缀名在空
            newname = portion[0] + ".txt"    # 要改的新后缀
            os.chdir(path)    # 切换文件路径如无路径则要新建或者路径同上，做好备份
            os.rename(filename, newname)

    return "{}任务完成".format(task)


def callback(future):    # 回调函数
    print("Callback: ", future.result())    # 返回任务结果


def  asyncio_work(task, path):
    coroutine = change_files(task, path)    # 定义协程并传入任务
    loop = asyncio.get_event_loop()    # 获得事件循环对象
    task = asyncio.ensure_future(coroutine)    # 获得任务对象（对协程的封装）
    task.add_done_callback(callback)    # 封装好后的协程对象（任务）就可以绑定回调函数了
    loop.run_until_complete(task)    # 执行协程任务

if __name__ == '__main__':
    task = str(input("请输入文件任务名："))
    path = str(input("请输入文件路径："))
    asyncio_work(task, path)
