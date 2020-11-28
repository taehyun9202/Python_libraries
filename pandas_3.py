import pandas as pd
import numpy as np

# df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index=[0, 1], columns=['a', 'b'])
# print(df)
#
# print(df['a'] <= 5)
#
# print(df.query("a <= 5 and b <= 8"))

# df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=['a', 'b', 'c', 'd'])
# print(df)
#
# df = df.apply(lambda x: x + 1)
# print(df)
#
#
# def add_one(x):
#     return x + 1
#
#
# df = df.apply(add_one)
# print(df)

# df = pd.DataFrame([
#         ['apple', 'peach', 'banana', 'orange'],
#         ['grape', 'apple', 'peach', 'acai']
#     ], index=[0, 1], columns=['a', 'b', 'c', 'd'])
#
# print(df)
# df = df.replace({'apple': 'pear'})
# print(df)

# df = pd.DataFrame([
#         ['apple', 8, 3, 'fruit'],
#         ['orange', 7, 4, 'fruit'],
#         ['carrot', 2, 6, 'vegetable'],
#         ['onion', 6, 5, 'vegetable']
#     ], columns=['name', 'count', 'price', 'type'])
#
# print(df)
# print(df.groupby(['type']).sum())
# print(df.groupby(['type']).aggregate([min, max, np.average]))
# print(df.groupby(['type']).aggregate([min, max, np.average]))
# print(df.groupby('type').get_group('fruit'))
#
#
# def my_filter(data):
#     return data['count'].mean() >= 5
#
#
# print(df.groupby('type').filter(my_filter))
#
# df['Gap'] = df.groupby('type')['count'].apply(lambda x: x - x.mean())
# print(df)

# df = pd.DataFrame(
#     np.random.randint(1, 10, (4, 4)),
#     index=[['first', 'first', 'second', 'second'], ['offense', 'defense', 'offense', 'defense']],
#     columns=['1', '2', '3', '4']
# )
#
# print(df)
# print(df[['1', '2']].loc['second'])


# df = pd.DataFrame([
#         ['apple', 8, 3, 'fruit'],
#         ['orange', 7, 4, 'fruit'],
#         ['peach', 4, 4, 'fruit'],
#         ['durian', 1, 8, 'fruit'],
#         ['carrot', 2, 6, 'vegetable'],
#         ['onion', 6, 4, 'vegetable'],
#         ['potato', 8, 4, 'vegetable'],
#         ['tomato', 4, 3, 'vegetable'],
#     ], columns=['name', 'count', 'price', 'type'])
#
# print(df)
# df = df.pivot_table(
#     index='price', columns='type', values='count', aggfunc=np.max
# )
# print(df)
