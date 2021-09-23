##################### 网络测速 #####################
# import speedtest
# # 全局取消证书验证
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# test = speedtest.Speedtest()
# download = test.download()
# upload = test.upload()
#
# print(f"上传速度：{round(upload/(1024*1024))}Mbps")
# print(f"下载速度：{round(down/(1024 * 1024),2)} Mbps")



##################### 获取本机局域网内IP #####################
import socket
hostn = socket.gethostname()
Laptop = socket.gethostbyname(hostn)
print("你的电脑本地IP地址为: ", Laptop)    # 局域网内IP



##################### 获取本机公网IP #####################
import json
from urllib.request import urlopen

# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# with urlopen(r'https://www.baidu.com') as fp:
with urlopen(r'https://jsonip.com') as fp:
    content = fp.read().decode()

ip = json.loads(content)['ip']
print("你的电脑公网IP地址是：", ip)