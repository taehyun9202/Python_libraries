import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3]
# y = [1, 2, 3]
# plt.plot(x, y)
# plt.title('plot')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig('plot.png')
# plt.show()

# x = np.linspace(0, np.pi * 10, 500)
# fig, axes = plt.subplots(2, 1)
# axes[0].plot(x, np.sin(x))
# axes[1].plot(x, np.cos(x))
# print(x)
# plt.show()

x = np.arange(-10, 11)
y1 = x ** 2
y2 = -2 * x
plt.plot(x, y1, linestyle=':', marker="*", color='red', label='y = x ** 2')
plt.plot(x, y2, linestyle='--', marker="o", color='blue', label='y = -2x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(
    shadow=True,
    borderpad=1
)
plt.show()