import threading    # 导入线程模块
print("当前线程为:", threading.current_thread())    # 对当前线程的查看
print("返回一个正运行线程的list:", threading.enumerate())    # 返回一个正运行线程的list
print("返回正在运行的线程数量:", threading.activeCount())    # 返回正在运行的线程数量，等于len(threading.enumerate())