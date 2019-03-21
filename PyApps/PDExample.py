import numpy as np, pandas as pd
import itertools

###own customized tools
from MyUtils import printnl

data = {"pos":[["A1","A2"],
               ["B1","B2"], 
               ['C1', 'C2']],
        "value"  :[[20200,10],
                 [20,50],
                 [1500, 1000]]}

data['count'] = [[(item >= 1000) + 1 for item in l_val]for l_val in data['value']]

# printnl(*data.items())

df = pd.DataFrame(data)
print(df)

for row in df.itertuples(index=False):
    print(row)
# print(list(df.itertuples(index=False)))