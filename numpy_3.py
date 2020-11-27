import numpy as np

# array = np.random.randint(1, 10, 10)
# np.save("saved.npy", array)
#
# result = np.load('saved.npy')
# print(result)

# array1 = np.arange(10)
# array2 = np.arange(10, 20)
#
# np.savez('saved', array1=array1, array2=array2)
# data = np.load('saved.npz')
# result1 = data['array1']
# result2 = data['array2']
# print(result1)
# print(result2)

# array = np.array([5, 7, 1, 4, 8])
# array.sort()
# print(array)
# print(array[::-1])

# array = np.array([[5, 6, 8, 2, 1], [7, 3, 5, 9, 4]])
# print(array)
# array.sort(axis=0)
# print(array)


# array = np.linspace(0, 10, 5)  # dtype=int)
# print(array)
#
# np.random.seed(7)
# print(np.random.randint(0, 10, (2, 3)))

array1 = np.arange(10)
array2 = array1
array2[0] = 99
print(array1)
print(array2)

array3 = array1.copy()
array3[0] = 15
print(array3)


array = np.array([1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6])
print(np.unique(array))
