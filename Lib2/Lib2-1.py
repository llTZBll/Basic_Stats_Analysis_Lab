import numpy as np
import matplotlib.pyplot as plt

# 定义区间I
I = np.linspace(-2*np.pi, 2*np.pi, 1000)

# 计算三角函数值
sin_values = np.sin(I)
cos_values = np.cos(I)
tan_values = np.tan(I)
# 处理tan函数的无穷大值
tan_values = np.clip(tan_values, -10, 10)  # 限制tan值范围以便显示

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(I, sin_values, linestyle='-', color='blue', label='sin(x)')
plt.plot(I, cos_values, linestyle='--', color='red', label='cos(x)')
plt.plot(I, tan_values, linestyle=':', color='green', label='tan(x)')

# 添加图例和标题
plt.legend()
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.ylim(-5, 5)  # 限制y轴范围
plt.show()