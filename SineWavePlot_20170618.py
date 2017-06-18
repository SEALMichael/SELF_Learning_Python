# -*- coding: utf-8 -*-
# =======================================================
# 2017/06/18
# 画正弦曲线小练习
# =======================================================
import matplotlib.pyplot as plt
import numpy as np

# Data to be represented
X = np.linspace(-np.pi, +np.pi, 256) # 设定X的范围以及在该区间内X所取的点的数目
# Y = np.sin(X)
Y = np.cos(X)                        # 直接使用numpy库中的正余弦计算

# Actual plotting
fig = plt.figure(figsize=(8, 6), dpi=100) # 设定图片大小以及像素
axes = plt.subplot(111)                   # 设定画图的布局
axes.plot(X, Y, color='black', linewidth=2, linestyle="-")
axes.set_xlim(X.min(), X.max())           # X坐标轴的范围
axes.set_ylim(-0.5+Y.min(), 0.5+Y.max())  # Y坐标轴的范围

plt.show()                                # 展示图片
