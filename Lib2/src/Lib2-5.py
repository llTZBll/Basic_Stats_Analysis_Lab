import numpy as np
import matplotlib.pyplot as plt

# 定义区间I
t = np.linspace(0, 10, 100)

# 计算坐标
x = np.sin(t) - t * np.cos(t)
y = np.cos(t) + t * np.sin(t)

# 创建图形
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# 1. 散点图
axes[0].scatter(x, y, c=t, cmap='viridis')
axes[0].set_title('Scatter Plot')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

# 2. 曲线图
axes[1].plot(x, y, 'b-')
axes[1].set_title('Line Plot')
axes[1].set_xlabel('x')

# 3. 阶梯图
axes[2].step(x, y, 'r-')
axes[2].set_title('Step Plot')
axes[2].set_xlabel('x')

plt.suptitle('Parametric Curves: x=sin(t)-t*cos(t), y=cos(t)+t*sin(t)')
plt.tight_layout()
plt.show()