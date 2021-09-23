import time
# time_time = time.time()
# print("time.time(): ", time_time)
#
# localtime = time.localtime()
# print("time.localtime(): ", localtime)

strftime = time.strftime("%Y-%m-%d %H:%M:%S")
print("time.strftime(): ", strftime)

timenow = time.time()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timenow)))