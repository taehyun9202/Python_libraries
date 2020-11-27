import pandas as pd
import numpy as np

# name_dict = {
#     'a': 'apple',
#     'b': 'banana',
#     'c': 'strawberry',
#     'd': 'orange',
#     'e': 'peach'
# }
#
# count_dict = {
#     'a': 3,
#     'b': 5,
#     'c': 7,
#     'd': 8,
#     'e': 6
# }
#
# price_dict = {
#     'a': 5,
#     'b': 3,
#     'c': np.nan,
#     'd': 9,
#     'e': 7
# }
#
# name = pd.Series(name_dict)
# count = pd.Series(count_dict)
# price = pd.Series(price_dict)
#
# summary = pd.DataFrame({
#     'name': name,
#     'count': count,
#     'price': price
# })
#
# print(summary)
# print(summary.notnull())
# print(summary.isnull())
#
# summary['count'] = summary['count'].fillna('no data')
# print(summary)
# summary = summary.fillna('no data')
# print(summary)
#
# summary = summary.sort_values('count', ascending=False)
# print(summary)


array1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
array2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

array_fill = array1.add(array2, fill_value=0)
print(array_fill)

array_no = array1.add(array2)
print(array_no)

array = array1 + array2
print(array)

array1 = pd.DataFrame([[1, 2], [3, 4]], index=['a', 'b'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['b', 'c', 'd'])

print(array1)
print(array2)
array = array1.add(array2, fill_value=0)
print(array)


print('sum of col1', array[1].sum())
print("total sum")
print(array.sum())
