import numpy as np

# list_data = [1, 2, 3]
# array = np.array(list_data)
# print(list_data)
# print(array)
# print(array.dtype)
# print(array.size)
# print(array[1])

# array1 = np.arange(4)
# print(array1)
#
# array2 = np.zeros((4, 4), dtype=float)
# print(array2)
#
# array3 = np.ones((3, 3), dtype=str)
# print(array3)
#
# array4 = np.random.randint(0, 10, (3, 3))
# print(array4)

# array5 = np.random.normal(0, 1, (3, 3))
# print(array5)

# array1 = np.array([1, 2, 3])
# array2 = np.array([4, 5, 6])
#
# array3 = np.concatenate([array1, array2])
# print(array3)
#
# array4 = array3.reshape((2, 3))
# print(array4)
#
# array5 = array3.reshape((3, 2))
# print(array5)

# array1 = np.arange(4).reshape(1, 4)
# array2 = np.arange(8).reshape(2, 4)
# print(array1, array2)
#
# array3 = np.concatenate([array1, array2], axis=0)
# print(array3)


array = np.arange(8).reshape(2, 4)
print(array)
left, right = np.split(array, [2], axis=1)
print(left.shape)
print(right.shape)
print(left)
print(right)
