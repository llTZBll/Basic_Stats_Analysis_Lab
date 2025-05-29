import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu, qr, svd
from matplotlib.gridspec import GridSpec
import os

os.makedirs('result1', exist_ok=True)
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

mean_value = 21

# 生成高斯矩阵
np.random.seed(42)
matrix = np.random.normal(mean_value, 1, size=(10, 15))

# LU分解
P, L, U = lu(matrix)
# QR分解
Q, R = qr(matrix)
# 奇异值分解
U_svd, s, Vt = svd(matrix)


# 可视化函数 - 在格子中显示数值
def visualize_matrix_with_values(ax, matrix, title, cmap='viridis'):
    im = ax.imshow(matrix, cmap=cmap)

    # 在每个格子中添加数值
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            text_color = 'black' if im.norm(matrix[i, j]) > 0.5 else 'white'
            ax.text(j, i, f'{matrix[i, j]:.2f}', ha='center', va='center', color=text_color, fontsize=6)

    ax.set_title(title)
    plt.colorbar(im, ax=ax)
    return im


# 图1：原始矩阵
fig1 = plt.figure(figsize=(12, 8))
ax1 = fig1.add_subplot(111)
visualize_matrix_with_values(ax1, matrix, '原始矩阵')
plt.tight_layout()
plt.savefig('result1/original_matrix.png', dpi=300, bbox_inches='tight')
plt.close(fig1)

# 图2：LU分解
fig2 = plt.figure(figsize=(18, 6))
gs2 = GridSpec(1, 3, figure=fig2)

ax_lu1 = fig2.add_subplot(gs2[0])
visualize_matrix_with_values(ax_lu1, P, '置换矩阵 P')

ax_lu2 = fig2.add_subplot(gs2[1])
visualize_matrix_with_values(ax_lu2, L, '下三角矩阵 L')

ax_lu3 = fig2.add_subplot(gs2[2])
visualize_matrix_with_values(ax_lu3, U, '上三角矩阵 U')

plt.tight_layout()
plt.savefig('result1/lu_decomposition.png', dpi=300, bbox_inches='tight')
plt.close(fig2)

# 图3：QR分解
fig3 = plt.figure(figsize=(12, 6))
gs3 = GridSpec(1, 2, figure=fig3)

ax_qr1 = fig3.add_subplot(gs3[0])
visualize_matrix_with_values(ax_qr1, Q, '正交矩阵 Q')

ax_qr2 = fig3.add_subplot(gs3[1])
visualize_matrix_with_values(ax_qr2, R, '上三角矩阵 R')

plt.tight_layout()
plt.savefig('result1/qr_decomposition.png', dpi=300, bbox_inches='tight')
plt.close(fig3)

# 图4：SVD分解
fig4 = plt.figure(figsize=(18, 12))
gs4 = GridSpec(2, 2, figure=fig4)

ax_svd1 = fig4.add_subplot(gs4[0, 0])
visualize_matrix_with_values(ax_svd1, U_svd, '左奇异矩阵 U')

ax_svd2 = fig4.add_subplot(gs4[0, 1])
# 奇异值向量需要转换为对角矩阵以便可视化
S = np.zeros((U_svd.shape[0], Vt.shape[1]))
np.fill_diagonal(S, s)
visualize_matrix_with_values(ax_svd2, S, '奇异值对角矩阵')

ax_svd3 = fig4.add_subplot(gs4[1, 0])
visualize_matrix_with_values(ax_svd3, Vt, '右奇异矩阵 V 的转置')

ax_svd4 = fig4.add_subplot(gs4[1, 1])
ax_svd4.plot(range(1, len(s) + 1), s, 'o-')
ax_svd4.set_title('奇异值分布')
ax_svd4.set_xlabel('奇异值序号')
ax_svd4.set_ylabel('奇异值大小')
ax_svd4.grid(True)

plt.tight_layout()
plt.savefig('result1/svd_decomposition.png', dpi=300, bbox_inches='tight')
plt.close(fig4)
