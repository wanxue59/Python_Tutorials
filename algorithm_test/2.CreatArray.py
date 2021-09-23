nums = list(map(int,input("请输入数组nums，并按Enter结束：").split(',')))
index = list(map(int,input("请输入数组index，并按Enter结束：").split(',')))
target = []
for i in range(len(index)):
    if index[i] == len(target):   # 当target的下标index[i]与target的长度相等时，使用append方法添加元素，若用index方法，会报错
        target.append(nums[i])
    else:
        target.insert(index[i], nums[i])
print(target)