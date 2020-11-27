import numpy as np

# array = np.random.randint(1, 10, size=4).reshape(2, 2)
# print(array)
#
# mul = array * 10
# print(mul)

# array1 = np.arange(4).reshape(2, 2)  # (2 * 2)
# array2 = np.arange(2)  # (1 * 2)
#
# array3 = array1 + array2
# print(array1)
# print(array2)
# print(array3)



# array1 = np.arange(0, 8).reshape(2, 4)
# array2 = np.arange(0, 8).reshape(2, 4)
#
# array3 = np.concatenate([array1, array2], axis=0)
# print(array3)
#
# array4 = np.arange(0, 4).reshape(4, 1)
# print(array4)
#
# print(array3 + array4)


# array1 = np.arange(16).reshape(4, 4)
# print(array1)
#
# array2 = array1 < 10
# print(array2)
#
# array1[array2] = 100
# print(array1)


array = np.arange(16).reshape(4, 4)
print(array)
print("max: ", np.max(array))
print("min: ", np.min(array))
print("sum: ", np.sum(array))
print("avg: ", np.mean(array))

print("sum of col: ", np.sum(array, axis=0))
print("sum of row: ", np.sum(array, axis=1))
