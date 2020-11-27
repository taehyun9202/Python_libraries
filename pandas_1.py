import pandas as pd

# array1 = pd.Series(['apple', 'banana', 'carrot'], index=['a', 'b', 'c'])
#
# print(array1)
# print(array1['a'])
#
# data = {
#     'a': 'apple',
#     'b': 'banana',
#     'c': 'carrot'
# }
#
# array2 = pd.Series(data)
# print(array2)
# print(array2['a'])

name_dict = {
    'a': 'apple',
    'b': 'banana',
    'c': 'carrot',
    'd': 'durian'
}

count_dict = {
    'a': 3,
    'b': 5,
    'c': 7,
    'd': 1
}

price_dict = {
    'a': 5,
    'b': 3,
    'c': 2,
    'd': 10
}

name = pd.Series(name_dict)
count = pd.Series(count_dict)
price = pd.Series(price_dict)

summary = pd.DataFrame({
    'name': name,
    'count': count,
    'price': price
})

summary.loc['a', 'price'] = 4
summary.loc['e'] = ['peach', 6, 5]
print(summary)

total = summary['count'] * summary['price']
summary['total'] = total
print(summary)


# slicing
# print(summary.loc['a':'c', 'price':])
# print(summary.iloc[1:3, 2:])

summary.to_csv('summary.csv', encoding='utf-8-sig')
saved = pd.read_csv('summary.csv', index_col=0)
print('*'*30)
print(saved)
