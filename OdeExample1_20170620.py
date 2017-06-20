# 计算一个二阶微分方程例子
# 2017年6月20日


import scipy.integrate
import pylab


# 返回值是y和y的导数组成的数组

def deriv(y, t):                                            # 输入是 Y=[y，dy]
    a = -2.0
    b = -0.1
    return pylab.array([y[1], a * y[0] + b * y[1]])               # 返回值是 DY = [dy, ddy]


time = pylab.linspace(0.0, 50.0, 10000)
y_init = pylab.array([0.0005, 0.2])  # 初值
y = scipy.integrate.odeint(deriv, y_init, time)

pylab.figure()
pylab.plot(time, y[:, 0], label='y')       # y[:,0]即返回值的第一列，是y的值。label是为了显示legend用的。
pylab.plot(time, y[:, 1], label="y'")      # y[:,1]即返回值的第二列，是y’的值
pylab.xlabel('t')
pylab.ylabel('y')
pylab.legend()
pylab.show()
