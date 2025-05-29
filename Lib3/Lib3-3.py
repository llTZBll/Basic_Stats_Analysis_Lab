import numpy as np
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 过去12个月生活花费数据
months = np.arange(1, 13)
costs = np.array([3500, 3800, 4200, 3300, 4500, 4800, 4200, 3500, 5300, 2800, 4000, 3200])

# 拟合一次曲线（线性）
p1 = np.polyfit(months, costs, 1)
f1 = np.poly1d(p1)

# 拟合二次曲线
p2 = np.polyfit(months, costs, 2)
f2 = np.poly1d(p2)

# 拟合三次曲线
p3 = np.polyfit(months, costs, 3)
f3 = np.poly1d(p3)

# 生成更多点用于绘制平滑曲线
x_fit = np.linspace(1, 12, 100)

# 绘制原始数据和拟合曲线
plt.figure(figsize=(10, 6))
plt.scatter(months, costs, color='black', label='原始数据')
plt.plot(x_fit, f1(x_fit), 'r-', label='一次曲线')
plt.plot(x_fit, f2(x_fit), 'g--', label='二次曲线')
plt.plot(x_fit, f3(x_fit), 'b-.', label='三次曲线')

plt.xlabel('月份')
plt.ylabel('生活花费（元）')
plt.title('过去12个月生活花费及拟合曲线')
plt.legend()
plt.grid(True)
plt.show()

# 输出拟合方程
print("一次曲线方程:")
print(f1)
print("\n二次曲线方程:")
print(f2)
print("\n三次曲线方程:")
print(f3)