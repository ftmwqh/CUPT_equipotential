import numpy as np
import matplotlib.pyplot as plt

m = 101
n = 101
U = np.zeros([m, n])
F = np.zeros([m, n])
# 定义边界条件
F[m - 1, :] = 100
e = 0.001
count = 0

for i in range(10000):
    count += 1
    F[:, 0] = 0
    F[:, n - 1] = 0
    F[0, :] = 0
    F[m - 1, :] = 100
    U[1:-1, 1:-1] = (F[1:-1, :-2] + F[1:-1, 2:] + F[:-2, 1:-1] + F[2:, 1:-1]) / 4
    e = abs(U - F).max()  # 求助老师我这个值为何总是0
    F = U

x = np.arange(0, m)
y = np.arange(0, n)
X, Y = np.meshgrid(x, y)
C = plt.contour(X, Y, U)
plt.clabel(C, inline=True, fontsize=10)
plt.show()

