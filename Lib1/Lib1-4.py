import numpy as np

np.random.seed(42)
vec1 = np.random.randn(100)
vec2 = np.random.randn(100)

print("原始向量1:", vec1[:5], "...")
print("原始向量2:", vec2[:5], "...")

# 交换偶数位（索引为1, 3, 5...）
vec1[1::2], vec2[1::2] = vec2[1::2], vec1[1::2]

print("交换后向量1:", vec1[:5], "...")
print("交换后向量2:", vec2[:5], "...")