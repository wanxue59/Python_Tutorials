"""
实例描述：
    通过编写爬虫，将指定日期时段的全部上市公司股票数据爬取下来，并按照股票代码保存到相应的Excel
文件中
"""
import urllib.request    # 网络请求模块
import re    # 正则表达式模块
stock_CodeUrl = "https://quote.eastmoney.com/center/gridlist.html#hs_a_board"    # 要爬取的地址
# stock_CodeUrl = "http://quote.eastmoney.com/usstocklist.html"    # 要爬取的地址
def urlTolist(url):    # 获取股票代码列表
    allCodeList = []
    html = urllib.request.urlopen(url).read()    # 请求链接，获取网页
    html = html.decode('gbk')    # 转码
    s = r'<li><a target="_blank" href="https://quote.eastmoney.com/unify/r/\S\S(.*?).html">'
    pat = re.compile(s)    # 创建正则表达式模板
    code = pat.findall(html)    # 正则表达式计算
    for item in code:
        if item[0] == '6' or item[0] == '3' or item[0] == '0':
            allCodeList.append(item)
    return allCodeList    # 返回结果


if __name__ == '__main__':
    allCodelist = urlTolist(stock_CodeUrl)    # 调用函数
    print(allCodelist[:10])    # 显示前10条数据