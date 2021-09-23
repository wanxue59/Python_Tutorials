n = int(input("请输入相邻字符的个数n，并按Enter结束："))
strings = str(input("请输入一串字符串，并按Enter结束："))
list1 = []
list2 = []
for i in range(len(strings)-n+1):
    s = strings[i:i+n]   # 使用切片提取相邻n个字符
    list1.append(s)   # 将每一个长度为n的子字符串作为一个元素添加到列表list1中，用于计数
    if list1.count(s) > 1:   # 按顺序将子字符串添加到列表list2中，并且每个子字符串只首次进入，重复字符串将不会再放入list2中，用于后续输出
        pass
    else:
        list2.append(s)
# print(list1)
# print(list2)

for j in range(len(list2)):
    a = list2[j]
    print(a, list1.count(a))
