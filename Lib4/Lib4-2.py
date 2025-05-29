import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 设置中文字体
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
column_names = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium',
                'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']
df = pd.read_csv(url, names=column_names)

# 准备数据
X = df.iloc[:, 1:].values  # 提取13个属性
y = df.iloc[:, 0].values   # 提取类别

# 数据标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 执行PCA
pca = PCA()
pca.fit(X_scaled)

# 计算累计贡献率
cumulative_variance = np.cumsum(pca.explained_variance_ratio_)

# 确定需要的主成分数量
n_components = np.argmax(cumulative_variance >= 0.9) + 1

# 使用确定的主成分数量重新执行PCA
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X_scaled)

print(f"提取了{n_components}个主成分，累计贡献率: {cumulative_variance[n_components-1]:.4f}")
print(f"原始数据形状: {X.shape}")
print(f"降维后数据形状: {X_pca.shape}")

# 创建画布
plt.figure(figsize=(20, 16))

# 1. 绘制解释方差比例
plt.subplot(2, 2, 1)
plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.7)
plt.step(range(1, len(cumulative_variance) + 1), cumulative_variance, where='mid', color='red', label='累计贡献率')
plt.axhline(y=0.9, color='g', linestyle='--', alpha=0.5)
plt.axvline(x=n_components, color='purple', linestyle='--', alpha=0.5)
plt.xticks(range(1, len(pca.explained_variance_ratio_) + 1))
plt.title('主成分解释方差比例与累计贡献率')
plt.xlabel('主成分')
plt.ylabel('解释方差比例')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# 2. 绘制前两个主成分的散点图
plt.subplot(2, 2, 2)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', alpha=0.8, s=50)
plt.title('前两个主成分的散点图')
plt.xlabel(f'主成分1 ({pca.explained_variance_ratio_[0]:.2%})')
plt.ylabel(f'主成分2 ({pca.explained_variance_ratio_[1]:.2%})')
plt.colorbar(scatter, label='葡萄酒类别')
plt.grid(True, linestyle='--', alpha=0.7)

# 3. 绘制前三个主成分的3D散点图
ax = plt.subplot(2, 2, 3, projection='3d')
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=y, cmap='viridis', alpha=0.8, s=50)
ax.set_title('前三个主成分的3D散点图')
ax.set_xlabel(f'主成分1 ({pca.explained_variance_ratio_[0]:.2%})')
ax.set_ylabel(f'主成分2 ({pca.explained_variance_ratio_[1]:.2%})')
ax.set_zlabel(f'主成分3 ({pca.explained_variance_ratio_[2]:.2%})')
plt.colorbar(scatter, ax=ax, label='葡萄酒类别')

# 4. 绘制载荷热图
plt.subplot(2, 2, 4)
loadings = pca.components_.T * np.sqrt(pca.explained_variance_)
loading_df = pd.DataFrame(loadings, columns=[f'主成分{i+1}' for i in range(n_components)],
                          index=column_names[1:])
sns.heatmap(loading_df, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('主成分载荷热图')

plt.tight_layout()
plt.savefig('wine_pca_visualization.png', dpi=300, bbox_inches='tight')
plt.show()