import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 生成3个有少量交叉的类
mean1, cov1 = [0, 0], [[1, 0.5], [0.5, 1]]
mean2, cov2 = [5, 2], [[1, -0.3], [-0.3, 1]]
mean3, cov3 = [2, 5], [[0.5, 0], [0, 2]]

class1 = np.random.multivariate_normal(mean1, cov1, 30)
class2 = np.random.multivariate_normal(mean2, cov2, 30)
class3 = np.random.multivariate_normal(mean3, cov3, 30)

# 合并所有数据点
X = np.vstack([class1, class2, class3])

# 创建一个2x2的子图布局
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 绘制原始数据
axes[0, 0].scatter(class1[:, 0], class1[:, 1], c='red', label='Class 1')
axes[0, 0].scatter(class2[:, 0], class2[:, 1], c='green', label='Class 2')
axes[0, 0].scatter(class3[:, 0], class3[:, 1], c='blue', label='Class 3')
axes[0, 0].set_title('原始数据分布')
axes[0, 0].legend()

# K-means聚类（k=3）
kmeans3 = KMeans(n_clusters=3, random_state=42)
y_pred3 = kmeans3.fit_predict(X)
axes[0, 1].scatter(X[:, 0], X[:, 1], c=y_pred3, cmap='viridis')
axes[0, 1].scatter(kmeans3.cluster_centers_[:, 0], kmeans3.cluster_centers_[:, 1], s=200, c='red', marker='X')
axes[0, 1].set_title('K-means聚类 (k=3)')

# K-means聚类（k=4）
kmeans4 = KMeans(n_clusters=4, random_state=42)
y_pred4 = kmeans4.fit_predict(X)
axes[1, 0].scatter(X[:, 0], X[:, 1], c=y_pred4, cmap='viridis')
axes[1, 0].scatter(kmeans4.cluster_centers_[:, 0], kmeans4.cluster_centers_[:, 1], s=200, c='red', marker='X')
axes[1, 0].set_title('K-means聚类 (k=4)')

# K-means聚类（k=5）
kmeans5 = KMeans(n_clusters=5, random_state=42)
y_pred5 = kmeans5.fit_predict(X)
axes[1, 1].scatter(X[:, 0], X[:, 1], c=y_pred5, cmap='viridis')
axes[1, 1].scatter(kmeans5.cluster_centers_[:, 0], kmeans5.cluster_centers_[:, 1], s=200, c='red', marker='X')
axes[1, 1].set_title('K-means聚类 (k=5)')

plt.tight_layout()
plt.show()