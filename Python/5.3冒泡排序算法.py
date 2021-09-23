# 冒泡排序算法
# numbers = [5, 1, 9, 7, 6, 4, 12, 45, 34]
numbers = input("请输入一串数字，用逗号隔开，输入完后请按Enter:").split(',')
numbers =[int(numbers[i]) for i in range(len(numbers))]   # 用for循环将列表中每个字符串数字转为整型
print("原始数据为：", numbers)
for i in range(len(numbers)-1):   # 外层循环，负责设置冒泡排序进行的次数
    for j in range(len(numbers)-i-1):   # 内层循环，负责将列表中相邻的两个元素进行比较，前i个不需要再比较了
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("排序后的数据为：", numbers)
