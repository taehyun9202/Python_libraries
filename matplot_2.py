import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(-10, 11)
# y1 = x ** 2
# plt.plot(
#     x, y1,
#     linestyle=':',
#     marker='o',
#     markersize=5,
#     markerfacecolor='blue',
#     markeredgecolor='red'
# )
#
# plt.show()

# x = np.arange(-10, 11)
# y1 = x ** 2
# plt.bar(x, y1, color='red')
# plt.show()

# x = np.random.randint(10)
# y = np.random.randint(10)
# z = np.random.randint(10)
# dt = [x, y, z]
# x_array = np.arange(10)
# for i in range(3):
#     plt.bar(
#         x_array,
#         dt[i],
#         bottom=np.sum(dt[:i], axis=0)
#     )
# plt.show()


x = np.random.rand(10)
y = np.random.rand(10)
print(x)
print(y)
colors = np.random.randint(0, 100, 10)
sizes = np.pi * 1000 * np.random.rand(10)
print(colors)
print(sizes)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)
plt.show()

