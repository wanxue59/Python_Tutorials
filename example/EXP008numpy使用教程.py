import numpy as np

data = np.empty(shape=(0, 1))    # 创建一个空数组--一列
data2 = np.array([[3], [4], [5]])
data3 = np.array([[1], [3], [4]])
data4 = np.array([2, 5, 7])
print(data)
# print(data2)
data = np.concatenate((data, data2))    # 将数组data2中的元素添加到数组data后面
print(data)
# data = np.append(data, 12)
# print(data)
data = np.empty(shape=(0, 1))
print(len(data))


raw_data = None
# print(len(raw_data))