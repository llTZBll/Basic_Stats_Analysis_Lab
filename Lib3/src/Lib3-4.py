import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 定义微分方程 dy/dx = (exp(x) - y) / x
def ode(x, y):
    return (np.exp(x) - y) / x

# 初始条件 y(1) = 2*exp(1)
x0 = 1
y0 = 2 * np.exp(1)

# 定义求解区间
x_span = [1, 10]
x_eval = np.linspace(1, 10, 100)  # 用于绘图的点

# 求解微分方程
sol = solve_ivp(ode, x_span, [y0], t_eval=x_eval, dense_output=True)

# 解析解
def analytical_solution(x):
    return (np.exp(x) + np.exp(1)) / x

# 绘制数值解和解析解
plt.figure(figsize=(10, 6))
plt.plot(sol.t, sol.y[0], 'b-', label='数值解')
plt.plot(x_eval, analytical_solution(x_eval), 'r--', label='解析解')
plt.xlabel('x')
plt.ylabel('y')
plt.title('微分方程 xy\' + y - exp(x) = 0 的解 (y(1) = 2e)')
plt.legend()
plt.grid(True)
plt.show()

# 输出特定点的解
print("当 x = 5 时，y 的数值解为:", sol.sol(5)[0])
print("当 x = 5 时，y 的解析解为:", analytical_solution(5))