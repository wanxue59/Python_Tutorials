import requests
import re
from bs4 import BeautifulSoup

# 创建正则表达式对象，表示规则
findLink = re.compile(r'"part":"(.*?)","duratio')

# 爬取网页数据，传入参数：网址
def fin_data(url):

    get_url = requests.get(url=url)                              # 此处不添加请求头，也可以正常爬取
    # print(get_url.text)                                        # 查看获取网页的源码--测试用

    bs_html = BeautifulSoup(get_url.text,"html.parser")          # 用html.parser解析器

    global url_title
    url_title_list = bs_html.get_text().title().split('\n',1)    # 分割标题，生成列表
    url_title = url_title_list[0][:-30].replace("/","")          # 提取标题，作为文件名使用

    print(url_title)
    bs_fin_data = bs_html.select('script')                       # 获取标签树

    bs_data = ''

    # 筛选列表数据
    for i in bs_fin_data:
        bs_data = str(i)
        if 'window.__INITIAL_STATE__={' in bs_data:
            # print(bs_data)                                     # 查看筛选的数据--测试用
            break

    # 正则查找，返回列表
    re_list = re.findall(findLink,bs_data)
    # print(re_list)                                             # 查看返回的列表--测试用

    return re_list


# 保存文件，传入参数：fin_data() 返回的列表
def save(video_list):
    file_title = "2020老男孩It教育最新Python3.8开发全套（学完可就业）.txt"    # 合成.txt格式 文件名
    # file_title = "newname.txt"
    name_file = open(file_title, "w",encoding="utf-8")            # 写入文件

    for i in video_list:
        name_file.write(i+"\n")

    name_file.close()


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV1Sp4y1U7Jr?p=344'
    video_list = fin_data(url)

    # 遍历列表
    for i in video_list:
        print(i)

    save(video_list)

