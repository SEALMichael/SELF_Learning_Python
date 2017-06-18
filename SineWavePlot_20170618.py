# -*- coding: utf-8 -*-
# =======================================================
# 2017/06/18
# 画正弦曲线小练习
# =======================================================
import matplotlib.pyplot as plt
import numpy as np

# Data to be represented
X = np.linspace(-np.pi, +np.pi, 256)
# Y = np.sin(X)
Y = np.cos(X)

# Actual plotting
fig = plt.figure(figsize=(8, 6), dpi=100)
axes = plt.subplot(111)
axes.plot(X, Y, color='black', linewidth=2, linestyle="-")
axes.set_xlim(X.min(), X.max())
axes.set_ylim(-0.5+Y.min(), 0.5+Y.max())

plt.show()
