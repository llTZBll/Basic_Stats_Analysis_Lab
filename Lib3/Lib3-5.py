from scipy.stats import binom
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 参数设置
n = 50  # 射击次数
p = 0.1  # 每次射击命中的概率

# 计算10次以上且40次以下的概率
k_values = range(11, 40)  # 范围是11到39（包含）
probability = sum(binom.pmf(k, n, p) for k in k_values)

print(f"射击50次，击中次数在10次以上且40次以下的概率为: {probability:.8f}")

# 可视化概率分布
import matplotlib.pyplot as plt
import numpy as np

k_all = np.arange(0, 51)
pmf_all = binom.pmf(k_all, n, p)

plt.figure(figsize=(12, 6))
plt.bar(k_all, pmf_all, width=0.8, alpha=0.7)
plt.axvline(x=10.5, color='r', linestyle='--', label='k=10')
plt.axvline(x=39.5, color='g', linestyle='--', label='k=39')
plt.xlabel('击中次数 k')
plt.ylabel('概率 P(X=k)')
plt.title(f'二项分布 B(n={n}, p={p})')
plt.legend()
plt.grid(True)
plt.show()