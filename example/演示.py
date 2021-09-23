import time
import os
file = "ZUUU27_2019-05-14_15:00:00_510.wav"
channel = str(file)[4:6]    # '27'
strpname = str(file)[7:-4].split('_')    # ['2019-05-14', '15:00:00', '510']
n_format = strpname[0] + " " + strpname[1].replace("-", ":")    # '2019-05-14 15:00:00'
asn_time1 = time.strptime(n_format, "%Y-%m-%d %H:%M:%S")
asn_time2 = time.mktime(asn_time1)    # 1557817200.0
asn_time3 = int(asn_time2) * 1000 + int(file[-7:-4])    # 1557817200510
new_filename = channel + str(asn_time3) + '.wav'    # '271557817200510.wav'
prefix = os.path.splitext(new_filename)    # ('271557817200510', '.wav')
# print("channel: ", channel)
# print("strpname: ", strpname)
# print("n_format: ", n_format)
# print("asn_time1: ", asn_time1)
# print("asn_time2: ", asn_time2)
# print("asn_time3: ", asn_time3)
# print("new_filename: ", new_filename)
# print("prefix: ", prefix)