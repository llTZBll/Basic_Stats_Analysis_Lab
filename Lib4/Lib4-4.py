import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)

# 生成两个完全不交叉的类
X, y = make_blobs(n_samples=60, centers=2, random_state=42, cluster_std=0.6, center_box=(0, 10))

# 创建并训练SVM分类器
clf = svm.SVC(kernel='linear', C=1000)
clf.fit(X, y)

# 绘制数据点和SVM决策边界
plt.figure(figsize=(10, 6))

# 绘制数据点
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)

# 绘制决策边界
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 创建网格来评估模型
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# 绘制决策边界和间隔
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# 绘制支持向量
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
           linewidth=1, facecolors='none', edgecolors='k', label='支持向量')

plt.title('SVM分类与支持向量')
plt.legend()
plt.show()

# 输出支持向量
print(f"支持向量数量: {len(clf.support_vectors_)}")
print("支持向量坐标:")
print(clf.support_vectors_)