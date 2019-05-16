import numpy as np, pandas as pd
import itertools, functools

###own customized tools
from MyUtils import printnl

#===============================================================================
# data = {"pos":[["A1","A2"],
#                ["B1","B2"], 
#                ['C1', 'C2']],
#         "value"  :[[20200,10],
#                  [20,50],
#                  [1500, 1000]]}
# 
# count = [[(item >= 1000) + 1 for item in l_val]for l_val in data['value']]
# max_count = functools.reduce(lambda x, y: [x[0] if x[0] > y[0] else y[0], x[1] if x[1] > y[1] else y[1]], count)
# 
# # printnl(*data.items())
# 
# df = pd.DataFrame(data)
# df['count'] = pd.Series(count)
# print(df)
# 
# new_count = []
# for row in df.itertuples(index=False):
# #     new_count.extend([row.value[i]/item if item 2 else  for i, item in enumerate(count)])
#     
#     print(row.value, row.count)
#===============================================================================

    
    
# print(list(df.itertuples(index=False)))

'''Unnesting'''
'''
Out[346]:
                 samples  subject  trial_num
0   [-0.3, -1.61, -0.14]        1          1
1   [-1.63, 0.02, -0.55]        1          2
2     [0.46, 1.12, 0.12]        1          3
3   [-2.73, -0.44, 2.26]        2          1
4  [-0.48, -0.13, -0.02]        2          2
5     [0.24, 0.43, 0.15]        2          3
'''    
dx = pd.DataFrame(
         {'trial_num': [1, 2, 3, 1, 2, 3],
          'subject': [1, 1, 1, 2, 2, 2],
          'samples': [[-0.3, -1.61, -0.14],
                      [-1.63, 0.02, -0.55],
                      [0.46, 1.12, 0.12],
                      [-2.73, -0.44, 2.26],
                      [-0.48, -0.13, -0.02],
                      [0.24, 0.43, 0.15]]
         }
     )  
  
 '''Method 1'''
cols_dct = {col: np.repeat(df[col].values, df['samples'].str.len()) for col in df.columns.drop('samples', 1)} #drop unnest columns, np.repeat values on the rest columns. if error cast int64 to int32, use .astype('int32')
cols_dct.update({'unnest': np.concatenate(df.samples.values)})  #or np.hstack()
df1 = pd.DataFrame(cols_dct)
 # print({'unnest': np.concatenate(df.samples.values)})
print(df1)
 
 '''Method 2'''
df1 = df.set_index(['subject', 'trial_num'])
df1 = pd.DataFrame(np.hstack(df1.samples.values), index=df1.index.repeat(df1.samples.str.len()), columns=['unnest']).reset_index()
###OR hstack/concatenate directly on series df1.samples
df1 = pd.DataFrame(np.hstack(df1.samples), index=df1.index.repeat(df1.samples.str.len()), columns=['unnest']).reset_index()
#####
df1 = pd.DataFrame(np.concatenate(df1.samples), index=df1.index.repeat(df1.samples.str.len()), columns=['unnest']).reset_index()
print(df1)
 
 '''Method 2a: unnesting to columns'''
pd.concat([pd.DataFrame(dx.samples.tolist()), dx.subject, dx.trial_num], axis=1)
######
pd.DataFrame(dx.samples.tolist(), index=pd.MultiIndex.from_tuples(list(zip(dx.subject, dx.trial_num)), names=['subject', 'trial_num'])).reset_index()
######
pd.DataFrame(np.hstack([dx.samples.tolist(), dx[['subject', 'trial_num']]]), columns=[0, 1, 2,'subject', 'trial_num'])
######
pd.DataFrame(np.hstack([dx.samples.tolist(), dx['subject'].values[:,None], dx['trial_num'].values[:,None]]), columns=[0, 1, 2,'subject', 'trial_num'])
###### adding a new dimension work directly to series and return ndarray with new dimension
pd.DataFrame(np.hstack([dx.samples.tolist(), dx['subject'][:,None], dx['trial_num'][:,None]]), columns=[0, 1, 2,'subject', 'trial_num'])
'''
Out[594]:
      0     1     2  subject  trial_num
0 -0.30 -1.61 -0.14        1          1
1 -1.63  0.02 -0.55        1          2
2  0.46  1.12  0.12        1          3
3 -2.73 -0.44  2.26        2          1
4 -0.48 -0.13 -0.02        2          2
5  0.24  0.43  0.15        2          3
''' 

'''Method 3'''
'''
Out[366]:
    var1  var2
0  a,b,c     1
1  c,d,e     2
'''
ds = pd.DataFrame({'var1': ['a,b,c', 'c,d,e'], 'var2': [1, 2]})
var1 = ds.var1.str.split(',', expand=True).values.ravel() #similar to .flatten(). Read https://stackoverflow.com/questions/28930465/what-is-the-difference-between-flatten-and-ravel-functions-in-numpy
var2 = np.repeat(ds.var2.values, len(var1)/len(ds))
ds1 = pd.DataFrame({'var1': var1, 'var2': var2})
print(ds1)

'''General unnesting function'''
def unnesting(df, explode):
    idx = df.index.repeat(df[explode[0]].str.len())
    df1 = pd.concat([
        pd.DataFrame({x: np.concatenate(df[x].values)}) for x in explode], axis=1)
    df1.index = idx
    return df1.join(df.drop(explode, 1), how='left')

