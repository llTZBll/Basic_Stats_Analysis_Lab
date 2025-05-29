import numpy as np
import matplotlib.pyplot as plt

# 原始数据
data = [13, 14, 20, 11, 20, 22, 36, 40, 25, 24, 25, 30, 33, 33,
        36, 32, 45, 43, 18, 10, 19, 20, 92, 40]

# （1）绘制直方图
plt.figure(figsize=(12, 6))

# 使用Sturges' formula确定合适的区间数量
k = int(np.ceil(np.log2(len(data))) + 1)
n, bins, patches = plt.hist(data, bins=k, edgecolor='black', alpha=0.7)

plt.title('Histogram of the Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# 显示直方图
plt.show()

# （2）数据分箱和均值平滑
# 使用与直方图相同的分箱边界
bin_means = []
smoothed_data = np.zeros_like(data, dtype=float)

for i in range(len(bins)-1):
    lower = bins[i]
    upper = bins[i+1]
    # 找出在当前区间的所有数据点
    in_bin = [x for x in data if lower <= x < upper] if i < len(bins)-2 else [x for x in data if lower <= x <= upper]
    if in_bin:
        bin_mean = np.mean(in_bin)
        bin_means.append(bin_mean)
        # 对区间内的数据进行均值平滑
        for j, x in enumerate(data):
            if (lower <= x < upper) if i < len(bins)-2 else (lower <= x <= upper):
                smoothed_data[j] = bin_mean

# 打印原始数据和平滑后的数据对比
print("原始数据和平滑后的数据对比:")
for orig, smoothed in zip(data, smoothed_data):
    print(f"原始: {orig:.1f} | 平滑: {smoothed:.1f}")

# 可视化原始数据和平滑后的数据
plt.figure(figsize=(12, 6))
plt.plot(data, 'bo-', label='Original Data')
plt.plot(smoothed_data, 'ro-', label='Smoothed Data')
plt.title('Original Data vs Smoothed Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()