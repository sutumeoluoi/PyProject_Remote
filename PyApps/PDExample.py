import numpy as np, pandas as pd
import itertools, functools

###own customized tools
from MyUtils import printnl

data = {"pos":[["A1","A2"],
               ["B1","B2"], 
               ['C1', 'C2']],
        "value"  :[[20200,10],
                 [20,50],
                 [1500, 1000]]}

count = [[(item >= 1000) + 1 for item in l_val]for l_val in data['value']]
max_count = functools.reduce(lambda x, y: [x[0] if x[0] > y[0] else y[0], x[1] if x[1] > y[1] else y[1]], count)

# printnl(*data.items())

df = pd.DataFrame(data)
df['count'] = pd.Series(count)
print(df)

new_count = []
for row in df.itertuples(index=False):
#     new_count.extend([row.value[i]/item if item 2 else  for i, item in enumerate(count)])
    
    print(row.value, row.count)

    
    
# print(list(df.itertuples(index=False)))