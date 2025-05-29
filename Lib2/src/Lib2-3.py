import numpy as np
import matplotlib.pyplot as plt

# 生成50个随机成绩(60-100之间)
np.random.seed(42)
scores = np.random.randint(60, 101, 50)

# 确定合理的区间
bins = [60, 70, 80, 90, 100]

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(scores, bins=bins, edgecolor='black', alpha=0.7)

# 添加标签和标题
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.title('Class Score Distribution (n=50)')
plt.grid(axis='y')

# 显示具体数值
for i in range(len(bins)-1):
    count = ((scores >= bins[i]) & (scores < bins[i+1])).sum()
    plt.text((bins[i]+bins[i+1])/2, count+0.5, str(count),
             ha='center', va='bottom')

plt.show()