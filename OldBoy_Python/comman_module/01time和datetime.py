"""
参考文档：常用模块-- by  linhaifeng
网址：https://www.cnblogs.com/linhaifeng/articles/6384466.html

在Python中，通常有这几种方式来表示时间：
    ·时间戳(timestamp)：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。
我们运行“type(time.time())”，返回的是float类型。
    ·格式化的时间字符串(Format String)
    ·结构化的时间(struct_time)：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，
秒，一年中第几周，一年中第几天，夏令时)
"""
import time
# --------------------------我们先以当前时间为准,让大家快速认识三种形式的时间
print("时间戳: ", time.time())    # 时间戳:1487130156.419527
# 格式化的时间字符串:'2017-02-15 11:40:53'
print("格式化的时间字符串: ", time.strftime("%Y-%m-%d %X"))

print("本地时区:", time.localtime())    #本地时区的struct_time
print("UTC时区:", time.gmtime())    #UTC时区的struct_time



"""
--------------------------按图1转换时间
    ·localtime([secs])：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准
    ·gmtime([secs])：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的
struct_time
    ·mktime(t)：将一个struct_time转化为时间戳。
    ·strftime(format[, t])：把一个代表时间的元组或者struct_time（如由time.localtime()和
time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一
个元素越界，ValueError的错误将会被抛出。
    ·time.strptime(string[, format])：把一个格式化时间字符串转化为struct_time。实际上它和strftime()
是逆操作。
    ·time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37,
                      tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)：
在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。
"""

time.localtime()
time.localtime(1473525444.037215)
print(time.mktime(time.localtime()))    # 1473525749.0
print(time.strftime("%Y-%m-%d %X", time.localtime()))    # 2016-09-11 00:49:56
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X'))




"""

--------------------------按图2转换时间
asctime([t]) : 
    把一个表示时间的元组或者struct_time表示为这种形式：'Sun Jun 20 23:21:05 1993'
    如果没有参数，将会将time.localtime()作为参数传入。
ctime([secs]) : 
    把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的
时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))
--------------------------其他用法
sleep(secs)：线程推迟指定的时间运行，单位为秒。
"""
print(time.asctime())    # Sun Sep 11 00:43:43 2016
print(time.ctime())  # Sun Sep 11 00:46:38 2016
print(time.ctime(time.time()))  # Sun Sep 11 00:46:38 2016