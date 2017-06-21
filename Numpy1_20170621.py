# Numpy是Python的一个很重要的库，很多科学计算的库都是以此为基础的
# 在使用之前我们需要先把它导入
# 2017年6月21日
# ================================================================
import numpy
from pylab import *
# from numpy import array, sin
# from numpy import *
a = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])   # 产生一维数组   数组的维数还不太理解，以及ndim的用法
aa = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])# 产生三维数组  ？？？？？？
print(aa[2:])                                      # 列出aa的除去前两个元素的其他元素
print(a)
print(type(aa))
print(a[0])               # 提取数组内第一个元素，是从0开始的
print(a[:2])              # 提取数组内前两个元素
print(a[-1])              # 提取数组内最后一个元素
print(a[-2:])             # 提取数组内最后两个元素
print(a[-3:])             # 提取数组内最后三个元素
print(a[1:])               # 取除了第一个元素以外的所有元素
print(a[:-1])              # 取除了最后一个元素外的所有元素
print(a[1:]-a[:-1])        # 后一个元素减去前一个元素
print(a[1:4])               # 索引数组中第2个元素到第4个元素
print(a[::2])               # 隔2个元素取值
print(a.shape)              # 查看数组的形状（行列）
a.shape = 2, 5              # 修改数组的形状（行列）
print(a)
print(a.shape)
# print(shape(a))
print(type(a))              # 查看数组的类型
print(a.size)               # 查看数组里面元素的数目
print(a.ndim)               # 查看数组的维数

e = numpy.array([4, 5, 6, 1, 2, 3])
print(e.ndim)

b = numpy.array([3, 4, 2])
print(a + b)              # 数组内对应元素相加
print(a * b)              # 数组内对应元素相乘
print(a ** b)             # 数组内对应元素乘方

c = numpy.linspace(-3.14, 2 * 3.14, 41)   # 利用linspace产生一系列的数据
print(sin(c))
d = sin(c)
e = cos(c)
print(c >= 0)            # 选取c中非负的数
mask = c >= 0

# 画图
figure()
plot(c[mask], 'ro')      # 画出所有对应的非负值的点
plot(d,  '*', e, 'ro')
title('What')
xlabel('x和')
ylabel('y')
show()
