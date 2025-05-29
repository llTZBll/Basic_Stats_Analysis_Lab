import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置中文字体支持
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 原始数据
data = np.array([
    # 年份, y, x1(国民总收入), x2(CPI增长率), x3(人均GDP)
    [1990, 14.39, 18718, 3.1, 1644],
    [1991, 12.98, 21826, 3.4, 1893],
    [1992, 11.60, 26937, 6.4, 2311],
    [1993, 11.45, 35260, 14.7, 2998],
    [1994, 11.21, 48108, 24.1, 4044],
    [1995, 10.55, 59811, 17.1, 5046],
    [1996, 10.42, 70142, 8.3, 5846],
    [1997, 10.06, 78061, 2.8, 6420],
    [1998, 9.14, 83024, 0.8, 6796],
    [1999, 8.18, 88479, 1.4, 7159],
    [2000, 7.58, 98000, 0.4, 7858],
    [2001, 6.95, 108068, 0.7, 8622],
    [2002, 6.45, 119096, 0.8, 9398],
    [2003, 6.01, 135174, 1.2, 10542],
    [2004, 5.87, 159587, 3.9, 12336],
    [2005, 5.89, 184089, 1.8, 14040]
])

# 将numpy数组转换为DataFrame并设置列名
df = pd.DataFrame(data, columns=['年份', '人口自然增长率', '国民总收入', 'CPI增长率', '人均GDP'])

# 准备自变量X和因变量y
X = df[['国民总收入', 'CPI增长率', '人均GDP']]
y = df['人口自然增长率']

# 建立线性回归模型
model = LinearRegression()
model.fit(X, y)

# 输出回归系数和截距
print("回归系数 (国民总收入, CPI增长率, 人均GDP):", model.coef_)
print("截距:", model.intercept_)
print(f"模型方程: 人口自然增长率 = {model.intercept_:.4f} + {model.coef_[0]:.4f}*国民总收入 + {model.coef_[1]:.4f}*CPI增长率 + {model.coef_[2]:.4f}*人均GDP")

# 可视化部分
plt.figure(figsize=(18, 5))

# 1. 绘制原始数据随年份变化趋势
plt.subplot(1, 2, 1)
plt.plot(df['年份'], df['人口自然增长率'], 'o-', label='人口自然增长率')
plt.xlabel('年份')
plt.ylabel('人口自然增长率')
plt.title('人口自然增长率随年份变化趋势')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)

# 2. 绘制预测值与实际值对比
plt.subplot(1, 2, 2)
y_pred = model.predict(X)
plt.scatter(y, y_pred)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel('实际值')
plt.ylabel('预测值')
plt.title('线性回归模型预测效果')
plt.grid(True)
plt.text(y.min(), y.max(), f'R方 = {model.score(X, y):.4f}', horizontalalignment='left', verticalalignment='top')

plt.show()