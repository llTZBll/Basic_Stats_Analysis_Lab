import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 十月份支出数据
categories = ['餐饮', '比赛', '交通', '娱乐', '水电费']  # 改为中文分类
expenses = [2500, 1200, 500, 800, 600]

# 创建3种不同风格的饼图
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# 1. 标准饼图
axes[0].pie(expenses, labels=categories, autopct='%1.1f%%')

# 2. 爆炸式饼图
explode = (0.1, 0.05, 0.05, 0.05, 0.05)
axes[1].pie(expenses, explode=explode, labels=categories,
           autopct='%1.1f%%', shadow=True)

# 3. 环形图
axes[2].pie(expenses, labels=categories, autopct='%1.1f%%',
           wedgeprops={'width':0.4})

plt.tight_layout()
plt.show()