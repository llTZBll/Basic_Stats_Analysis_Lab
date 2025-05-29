import numpy as np
# 假设的12个月生活花费数据（实际使用时请替换为真实数据）
costs = np.array([3500, 3800, 4200, 3300, 4500, 4800, 4200, 3500, 5300, 2800, 4000, 3200])

# 计算均值的极大似然估计
mu_mle = np.mean(costs)

# 计算方差的极大似然估计
sigma2_mle = np.mean((costs - mu_mle) ** 2)

print(f"均值的极大似然估计: {mu_mle:.2f}")
print(f"方差的极大似然估计: {sigma2_mle:.2f}")
print(f"标准差的极大似然估计: {np.sqrt(sigma2_mle):.2f}")

# 可视化数据和估计的正态分布
import matplotlib.pyplot as plt
from scipy.stats import norm
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
plt.hist(costs, bins=6, density=True, alpha=0.6, color='g', label='数据直方图')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu_mle, np.sqrt(sigma2_mle))
plt.plot(x, p, 'k', linewidth=2, label='估计的正态分布')

plt.xlabel('生活花费（元）')
plt.ylabel('概率密度')
plt.title('生活花费数据的正态分布拟合')
plt.legend()
plt.grid(True)
plt.show()