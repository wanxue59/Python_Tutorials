"""
机器学习实战：从一组看似混乱的数据中找出y≈2x的规律
实例描述：
    假设有这么一组数据集，看上去很混乱，但x和y存在着固定的关系。本例就是让机器学习算法来
学习这些样本，并能够找到其中的规律。
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
### 样本准备 ###
train_X = np.linspace(-1, 1, 100)
train_Y = 2*train_X +  np.random.randn(*train_X.shape)*3    # y=2x，但是加了噪声

### 显示模拟数据点 ###
# plt.plot(train_X, train_Y, 'ro', label='Original data')
# plt.legend()    # 显示标注
# plt.show()    # 生成坐标图

### 线性回归模型 ###
model = LinearRegression()    # 将模型实例化
model.fit(train_X.reshape(100, 1), train_Y.reshape(100, 1))    # 进行训练
print("输入6的模型预测结果：", model.predict(6))    # 使用模型预测结果
print("线性模型的斜率: {}\t截距: {}".format(model.coef_, model.intercept_))
print("使用斜率与截距的计算结果: ", model.coef_*6 + model.intercept_)    # y=kx+b

### 将模型可视化 ###
plt.plot(train_X, train_Y, 'ro', label='Original data')    # 显示样本
plt.plot(train_X, model.predict(train_X.reshape(100, 1)), label='Fitted line')
plt.legend()    # 显示标注
plt.show()    # 生成坐标图