array = list(map(int,input("请输入数组nums，并按Enter结束：").split(',')))
K = int(input("请输入整数K，并按Enter结束："))
new_array = []   # 新列表，之后装入最强K个值
array = sorted(array)   # 对输入列表由小到大排序
m = array[(len(array)-1)//2]   # 求出排序后列表的中位值

for i in range(len(array)-1):   # 根据给定“强”的定义，使用冒泡算法对列表进行排序
    for j in range(len(array)-i-1):
        if abs(array[j] - m) > abs(array[j+1] - m) or abs(array[j] - m) == abs(array[j+1] - m) and array[j] > array[j+1]:   # “强”的判定条件
            array[j], array[j+1] = array[j+1], array[j]   # 冒泡算法后列表的值是由“弱”到“强”排序

# a = [5, 7, 9, 8, 4, 1]
array = list(reversed(array))   # 将列表逆序，由“强”到“弱”排序
for i in range(K):
    new_array.append(array[i])   # 将前K个最“强”值添加到新列表中
print(new_array)
