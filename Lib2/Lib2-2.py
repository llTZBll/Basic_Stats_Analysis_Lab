import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义区间I
t = np.linspace(0, 10*np.pi, 1000)

# 计算坐标
x = np.sin(t) - t * np.cos(t)
y = np.cos(t) + t * np.sin(t)
z = t

# 创建3D图形
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制曲线
ax.plot(x, y, z, linewidth=2)

# 设置z轴为对数刻度
ax.set_zscale('log')

# 添加网格和标签
ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z (log scale)')
ax.set_title('3D Spiral with Logarithmic Z-axis')

plt.show()