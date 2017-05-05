import matplotlib.pyplot as plt
import math
import numpy as np


def f(x):
    y = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
    return y


f_vals = []
x_vals = []
for i in range(0, 10000):
    f_vals.append(f(i / 1000))
    x_vals.append(i / 1000)
index = f_vals.index(max(f_vals))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(0)
plt.plot(x_vals, f_vals)
plt.scatter(
    [
        x_vals[index],
    ], [
        f_vals[index],
    ], 30, color='red')
plt.annotate(
    r'f=' + str(f_vals[index]),
    xy=(x_vals[index], f_vals[index]),
    xycoords='data',
    xytext=(+10, +30),
    textcoords='offset points',
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.xlabel('x')
plt.ylabel('f')
plt.title('$f(x)=x+10sin5x+7con4x$')  # 添加图形标题
plt.grid()
plt.legend()
plt.show()