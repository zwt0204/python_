# -*- encoding: utf-8 -*-
"""
@File    : Broadcasting.py
@Time    : 2020/3/16 13:41
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import numpy as np

#
# a = np.arange(12) ** 2
# print(a)
# i = np.array([1, 1, 3, 8, 5])
# print(a[i])
# j = np.array([[3, 4], [9, 7]])
# # print(a[j])
#
# palette = np.array([[0, 0, 0],
#                     [255, 0, 0],
#                     [0, 255, 0],
#                     [0, 0, 255],
#                     [255, 255, 255]])
# image = np.array([[0, 1, 2, 0],
#                   [0, 3, 4, 0]])
# print(palette[image])   # (2, 4, 3)

# a = np.arange(12).reshape(3, 4)
# print(a)
i = np.array([[0, 1],  # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])

# print(a[i, j])

time = np.linspace(20, 145, 5)
# print(time)
data = np.sin(np.arange(20)).reshape(5, 4)
# print(data)
ind = data.argmax(axis=0)
# print(ind)

time_max = time[ind]
# print(time_max)
# print(range(data.shape[1]))
data_max = data[ind, range(data.shape[1])]
# print(data_max)


# a = np.arange(5)
# print(a)
# a[[0, 0, 2]] = [1, 2, 3]
# print(a)

# a[[0, 0, 2]] += 1
# print(a)

# a = np.arange(12).reshape(3, 4)
# print(a)
# b = a > 4
# print(b)
# print(a[b])
# a[b] = 0
# print(a)
import matplotlib.pyplot as plt


def mandebrot(h, w, maxit=20):
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime==maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime


if __name__ == '__main__':
    # plt.imshow(mandebrot(400, 400))
    # plt.show()
    pass
    # a = np.array([2, 3, 4, 5])
    # b = np.array([8, 5, 4])
    # c = np.array([5, 4, 6, 8, 3])
    # ax, bx, cx = np.ix_(a, b, c)
    # print(ax)
    # result = ax + bx * cx
    # print(result)
    # a = np.array([[1.0, 2.0], [3.0, 4.0]])
    # print(a)
    # 矩阵转置
    # print(a.transpose())
    # 矩阵求逆运算
    # print(np.linalg.inv(a))
    # 单位矩阵
    # print(np.eye(2))
    # 矩阵的迹
    # print(np.trace(np.eye(2)))
    # 求解线性方程组， a为矩阵，b为一维或者二维数组
    # np.linalg.solve(a, y)
    """
    使用eig函数求解特征值和特征向量:np.linalg.eig(j)
    """
    # 自动整形
    a = np.arange(30)
    a.shape = 2, -1, 3
    # print(a.shape)
    # 矢量堆叠 vstack、hstack
    import numpy as np
    import matplotlib.pyplot as plt
    # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
    mu, sigma = 2, 0.5
    # 均值为mu，方差为sigma的正态分布
    v = np.random.normal(mu, sigma, 10000)
    # Plot a normalized histogram with 50 bins
    # 直方图， bins:条形的个数， normed：是否标准化
    plt.hist(v, bins=50, density=1)  # matplotlib version (plot)
    # plt.show()

    (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
    plt.plot(.5 * (bins[1:] + bins[:-1]), n)
    # plt.show()

    # 较小的数组在较大的数组上广播
    a = np.array([0.0, 10.0, 20.0, 30.0])
    # print(a)
    b = np.array([1.0, 2.0, 3.0])
    # print(b)
    # print(a[:, np.newaxis])
    # print(a[:, np.newaxis] + b)


