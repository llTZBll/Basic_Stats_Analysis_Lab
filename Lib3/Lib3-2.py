import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from mpl_toolkits.mplot3d import Axes3D

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义线性规划问题
c = [-1, -0.8, -1.2]
A = [[1, -1, 1], [3, 2, 4], [3, 2, 0]]
b = [30, 42, 30]

# 求解线性规划
res = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)]*3, method='highs')

# 输出结果
print("最优解:")
print(f"X1 = {res.x[0]:.4f}")
print(f"X2 = {res.x[1]:.4f}")
print(f"X3 = {res.x[2]:.4f}")
print(f"目标函数最小值 Z = {-res.fun:.4f}")  # 注意目标函数是求最小化，输出时取负

print("\n有效约束（等号成立的约束）:")
tolerance = 1e-9
for i in range(len(A)):
    constraint_value = sum(A[i][j] * res.x[j] for j in range(3))
    if abs(constraint_value - b[i]) < tolerance:
        print(f"约束 {i+1}: {constraint_value:.4f} = {b[i]} (有效)")
    else:
        print(f"约束 {i+1}: {constraint_value:.4f} < {b[i]} (非有效)")

# 三维可视化
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# 定义网格范围（根据最优解调整）
x = np.linspace(0, 5, 100)
y = np.linspace(10, 20, 100)
X, Y = np.meshgrid(x, y)

# 约束1: X1 - X2 + X3 <= 30 → X3 <= 30 - X1 + X2
Z1 = 30 - X + Y
Z1[Z1 < 0] = np.nan  # 忽略负值
ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue', label='约束1: X1 - X2 + X3 ≤ 30')

# 约束2: 3X1 + 2X2 + 4X3 <= 42 → X3 <= (42 - 3X1 - 2X2)/4
Z2 = (42 - 3*X - 2*Y) / 4
Z2[Z2 < 0] = np.nan
ax.plot_surface(X, Y, Z2, alpha=0.5, color='green', label='约束2: 3X1 + 2X2 + 4X3 ≤ 42')

# 约束3: 3X1 + 2X2 <= 30 → 垂直于X3的平面
Z3 = np.linspace(0, 10, 100)  # X3范围
X3, Z3 = np.meshgrid(x, Z3)
Y3 = (30 - 3*X3) / 2  # 从约束3解出Y
mask = (Y3 >= 10) & (Y3 <= 20)  # 限制Y范围
Y3[~mask] = np.nan
ax.plot_surface(X3, Y3, Z3, alpha=0.5, color='red', label='约束3: 3X1 + 2X2 ≤ 30')

# 绘制最优解点
ax.scatter(res.x[0], res.x[1], res.x[2], color='black', s=200,
           label=f'最优解: ({res.x[0]:.1f}, {res.x[1]:.1f}, {res.x[2]:.1f})')

# 设置图形属性
ax.set_xlabel('X1', fontsize=12)
ax.set_ylabel('X2', fontsize=12)
ax.set_zlabel('X3', fontsize=12)
ax.set_title('线性规划三维可视化（最优解在约束2和约束3的交点）', fontsize=14)
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()