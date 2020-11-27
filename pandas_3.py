import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index=[0, 1], columns=['a', 'b'])
print(df)

print(df['a'] <= 5)

print(df.query("a <= 5 and b <= 8"))
