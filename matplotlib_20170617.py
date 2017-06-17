# -*- coding: UTF-8 -*-
# ==========================================================
# 2017年6月17日
# 想学python
# ==========================================================
# from sympy import integrate, exp, sin, log, oo, pi,symbols
# import keyword
#
# x, y = symbols('x,y')  # 定义符号变量x,y
#
# # 求不定积分
# integrate(6*x**5, x)
# integrate(log(x), x)
#
# print("Hello World!")
# for i in range(1, 15):
#     print(i)
#
# else:
#     print("the for loop is over")

import matplotlib
import numpy
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
DataX = [1, 2, 3, 4, 5, 6, 7]
DataY = [7, 6, 5, 4, 3, 2, 1]
ax.scatter(DataX, DataY, 15.0 * numpy.array(DataX), 15.0 * numpy.array(DataY))
plt.show()
