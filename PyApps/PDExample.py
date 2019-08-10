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
#===============================================================================
# Out[346]:
#                  samples  subject  trial_num
# 0   [-0.3, -1.61, -0.14]        1          1
# 1   [-1.63, 0.02, -0.55]        1          2
# 2     [0.46, 1.12, 0.12]        1          3
# 3   [-2.73, -0.44, 2.26]        2          1
# 4  [-0.48, -0.13, -0.02]        2          2
# 5     [0.24, 0.43, 0.15]        2          3
# '''    
# dx = pd.DataFrame(
#          {'trial_num': [1, 2, 3, 1, 2, 3],
#           'subject': [1, 1, 1, 2, 2, 2],
#           'samples': [[-0.3, -1.61, -0.14],
#                       [-1.63, 0.02, -0.55],
#                       [0.46, 1.12, 0.12],
#                       [-2.73, -0.44, 2.26],
#                       [-0.48, -0.13, -0.02],
#                       [0.24, 0.43, 0.15]]
#          }
#      )  
#    
# '''Method 1'''
# cols_dct = {col: np.repeat(df[col].values, df['samples'].str.len()) for col in df.columns.drop('samples', 1)} #drop unnest columns, np.repeat values on the rest columns. if error cast int64 to int32, use .astype('int32')
# cols_dct.update({'unnest': np.concatenate(df.samples.values)})  #or np.hstack()
# df1 = pd.DataFrame(cols_dct)
#  # print({'unnest': np.concatenate(df.samples.values)})
# print(df1)
#   
#  '''Method 2'''
# df1 = df.set_index(['subject', 'trial_num'])
# df1 = pd.DataFrame(np.hstack(df1.samples.values), index=df1.index.repeat(df1.samples.str.len()), columns=['unnest']).reset_index()
# ###OR hstack/concatenate directly on series df1.samples
# df1 = pd.DataFrame(np.hstack(df1.samples), index=df1.index.repeat(df1.samples.str.len()), columns=['unnest']).reset_index()
# #####
# df1 = pd.DataFrame(np.concatenate(df1.samples), index=df1.index.repeat(df1.samples.str.len()), columns=['unnest']).reset_index()
# print(df1)
#   
#  '''Method 2a: unnesting to columns'''
# pd.concat([pd.DataFrame(dx.samples.tolist()), dx.subject, dx.trial_num], axis=1)
# ######
# pd.DataFrame(dx.samples.tolist(), index=pd.MultiIndex.from_tuples(list(zip(dx.subject, dx.trial_num)), names=['subject', 'trial_num'])).reset_index()
# ######
# pd.DataFrame(np.hstack([dx.samples.tolist(), dx[['subject', 'trial_num']]]), columns=[0, 1, 2,'subject', 'trial_num'])
# ######
# pd.DataFrame(np.hstack([dx.samples.tolist(), dx['subject'].values[:,None], dx['trial_num'].values[:,None]]), columns=[0, 1, 2,'subject', 'trial_num'])
# ###### adding a new dimension work directly to series and return ndarray with new dimension
# pd.DataFrame(np.hstack([dx.samples.tolist(), dx['subject'][:,None], dx['trial_num'][:,None]]), columns=[0, 1, 2,'subject', 'trial_num'])
# '''
# Out[594]:
#       0     1     2  subject  trial_num
# 0 -0.30 -1.61 -0.14        1          1
# 1 -1.63  0.02 -0.55        1          2
# 2  0.46  1.12  0.12        1          3
# 3 -2.73 -0.44  2.26        2          1
# 4 -0.48 -0.13 -0.02        2          2
# 5  0.24  0.43  0.15        2          3
# ''' 
# 
# '''Method 3'''
# '''
# Out[366]:
#     var1  var2
# 0  a,b,c     1
# 1  c,d,e     2
# '''
# ds = pd.DataFrame({'var1': ['a,b,c', 'c,d,e'], 'var2': [1, 2]})
# var1 = ds.var1.str.split(',', expand=True).values.ravel() #similar to .flatten(). Read https://stackoverflow.com/questions/28930465/what-is-the-difference-between-flatten-and-ravel-functions-in-numpy
# var2 = np.repeat(ds.var2.values, len(var1)/len(ds))
# ds1 = pd.DataFrame({'var1': var1, 'var2': var2})
# print(ds1)
#===============================================================================

'''
Special case (two columns type object same list size on same row) unnesting function
pd.DataFrame({'A':[1,2],'B':[[1,2, 3],[3,4]],'C':[[1,2, 5],[3,4]]})
NOTE: it only work on first col specify in 'explode' has longest list
  ex: eplode = ['B','C'] 

Out[592]: #Work
   A       B       C
0  1  [1, 2, 3]  [1, 2, 5]
1  2  [3, 4]  [3, 4]

Out[592]: #Work!!
   A       B       C
0  1  [1, 2, 3]  [1, 2]     #longest
1  2  [3, 4]  [3, 4]

Out[592]: #Doesn't work!!
   A       B       C
0  1  [1, 2]  [1, 2]
1  2  [3, 4]  [3, 4, 5]    #longest

'''
#===============================================================================
# def unnesting(df, explode):
#     idx = df.index.repeat(df[explode[0]].str.len().astype('int32'))
#     df1 = pd.concat([
#         pd.DataFrame({x: np.concatenate(df[x].values)}) for x in explode], axis=1)
#     df1.index = idx
#     return df1.join(df.drop(explode, 1), how='left')
# 
# '''Andy unnest version'''
# def explode(df, col_names):
#     
#     list_len = df[col_names[0]].str.len().astype('int32')
# #    d1 = pd.DataFrame({col: np.concatenate(df[col].values) 
# #                    for col in col_names})
# #    d2 = pd.DataFrame({x: np.repeat(df[x].values, list_len) 
# #                            for x in df.columns.difference(col_names)})                    
# #    df_exp = pd.concat([d1, d2], axis=1)    
# #    df_exp.index = idx
# 
#     idx = df.index.repeat(list_len)
#     d1 = {col: np.concatenate(df[col].values) 
#             for col in col_names}
#     d2 = {x: np.repeat(df[x].values, list_len) 
#             for x in df.columns.difference(col_names)}
#     d1.update(d2)        
#     
#     df_exp = pd.DataFrame(d1, index=idx)
#         
#     return df_exp
#===============================================================================

'''Andy unnest all'''
'''
   A          B             C
0  1  [1, 2, 3]        [1, 2]
1  2     [3, 4]  [3, 4, 5, 6]

To:
   A  B  C
0  1  1  1
0  1  1  2
0  1  2  1
0  1  2  2
0  1  3  1
0  1  3  2
1  2  3  3
1  2  3  4
1  2  3  5
1  2  3  6
1  2  4  3
1  2  4  4
1  2  4  5
1  2  4  6
'''
#===============================================================================
# def explode_all(df, col_names):
#     d = df.to_dict('list')
#     idx = df.index
#     
#     for i, col in enumerate(col_names):
#         dfcols_idx = df.columns.difference([col])
#         col_len = list(map(len, d[col]))
#         idx = idx.repeat(col_len)
#         d1 = {col: np.concatenate(d[col]).tolist()} 
#             
#         d2 = {x: np.repeat(d[x], col_len).tolist() for x in dfcols_idx}
#         
#         d.update(d1)
#         d.update(d2)
#                 
# #     for col in col_names:
# #         df = explode(df, [col])
#     df_exp = pd.DataFrame(d, index=idx)
#     return df_exp 
#===============================================================================

###testing
#===============================================================================
# df = pd.DataFrame({'A':[1,2],'B':[[1,2, 3],[3,4]],'C':[[1,2, 5],[3,4]]})
# print(df)
# print(explode_all(df, ['B', 'C']))
#===============================================================================


'''Same constrain as unnesting()'''
def explode_more(df, col_names):
    data = np.concatenate(df[col_names].values.tolist(), axis=1).T
#     data = np.column_stack(df[col_names].values.tolist()).T #column_stack on 2d is like hstack
#     data = np.hstack(df[col_names].values.tolist()).T   
    list_len = df[col_names[0]].str.len()
    new_idx = df.index.repeat(list_len)
    
    return df.drop(col_names, 1).join(pd.DataFrame(data, index=new_idx, columns=col_names))

'''vstack, hstack, stack
In [589]: a = np.array([[0, 3],
     ...:        [1, 4],
     ...:        [2, 5]])
     ...:

In [590]: b = np.array([[ 6,  9],
     ...:        [ 7, 10],
     ...:        [ 8, 11]])

a.shape => (3, 2)
b.shape => (3, 2)     
     
vstack: double element of axis=0: np.vstack([a,b]).shape =>  (6, 2) (already 2d, so doesn't create new dim, just double it)
hstack: double element of axis=1: np.hstack([a,b]).shape =>  (3, 4)
stack: axis=0: create new axis 0 = 2: np.stack([a,b], axis=0).shape => (2, 3, 2)
stack: axis=1: create new axis 1 = 2: np.stack([a,b], axis=1).shape => (3, 2, 2)
stack: axis=2: create new axis 2 = 2: np.stack([a,b], axis=2).shape => (3, 2, 2)
Note: 
_ stack create 1 more dimension so stack on 2ds creating 3d and max axis allowed is 2. Stack 3ds creating 4d 
      and max axis allow is 3 so on and so forth
_ vstack and hstack DON'T create dimension if array dimension >= 2, just double size on specified axis.
  If array = 1d, vstack create new dimension on axis 0 while hstack DOESN'T      
'''

'''np.concatenate, vstack, hstack, dstack
np.concatenate: go to specified axis/level picking all items of each array of that axis/level and join the same of each array. Going up one level and do it again.
vstack: doing the same as np.concatenate specified axis=0 
hstack: doing the same as np.concatenate specified axis=1
dstack: doing the same as np.concatenate specified axis=2

In [1904]: t1
Out[1904]:
[[[[1, 2, 3], [1, 0, 2], [1, 0, 2]],
  [[1, 2, 3], [2, 4, 5], [2, 4, 5]],
  [[1, 2, 3], [2, 2, 7], [2, 2, 7]],
  [[1, 2, 3], [2, 3, 3], [2, 3, 3]],
  [[1, 2, 3], [4, 1, 2], [4, 1, 2]],
  [[1, 2, 3], [4, 7, 3], [4, 7, 3]]],
 [[[1, 2, 3], [1, 0, 2], [1, 0, 2]],
  [[1, 2, 3], [2, 4, 5], [2, 4, 5]],
  [[1, 2, 3], [2, 2, 7], [2, 2, 7]],
  [[1, 2, 3], [2, 3, 3], [2, 3, 3]],
  [[1, 2, 3], [4, 1, 2], [4, 1, 2]],
  [[1, 2, 3], [4, 7, 3], [4, 7, 3]]]]
  
Below is True for 2d arrays up. On 1d arrays, they are diff: 
np.concatenate(t1, axis=0) ==  np.vstack(t1)
np.concatenate(t1, axis=1) ==  np.hstack(t1) 
np.concatenate(t1, axis=2) ==  np.dstack(t1)

On 1d arrays:
array([[1, 0, 3],
       [1, 1, 2]])

np.concatenate(a, axis=0) ==  np.hstack(a)       
  
'''
  
np.concatenate(t1, axis=0)
'''
array([[[1, 2, 3],
        [1, 0, 2],
        [1, 0, 2]],

       [[1, 2, 3],
        [2, 4, 5],
        [2, 4, 5]],

       [[1, 2, 3],
        [2, 2, 7],
        [2, 2, 7]],

       [[1, 2, 3],
        [2, 3, 3],
        [2, 3, 3]],

       [[1, 2, 3],
        [4, 1, 2],
        [4, 1, 2]],

       [[1, 2, 3],
        [4, 7, 3],
        [4, 7, 3]],

       [[1, 2, 3],
        [1, 0, 2],
        [1, 0, 2]],

       [[1, 2, 3],
        [2, 4, 5],
        [2, 4, 5]],

       [[1, 2, 3],
        [2, 2, 7],
        [2, 2, 7]],

       [[1, 2, 3],
        [2, 3, 3],
        [2, 3, 3]],

       [[1, 2, 3],
        [4, 1, 2],
        [4, 1, 2]],

       [[1, 2, 3],
        [4, 7, 3],
        [4, 7, 3]]])
'''
        
np.concatenate(t1, axis=1)
'''
array([[[1, 2, 3],
        [1, 0, 2],
        [1, 0, 2],
        [1, 2, 3],
        [1, 0, 2],
        [1, 0, 2]],

       [[1, 2, 3],
        [2, 4, 5],
        [2, 4, 5],
        [1, 2, 3],
        [2, 4, 5],
        [2, 4, 5]],

       [[1, 2, 3],
        [2, 2, 7],
        [2, 2, 7],
        [1, 2, 3],
        [2, 2, 7],
        [2, 2, 7]],

       [[1, 2, 3],
        [2, 3, 3],
        [2, 3, 3],
        [1, 2, 3],
        [2, 3, 3],
        [2, 3, 3]],

       [[1, 2, 3],
        [4, 1, 2],
        [4, 1, 2],
        [1, 2, 3],
        [4, 1, 2],
        [4, 1, 2]],

       [[1, 2, 3],
        [4, 7, 3],
        [4, 7, 3],
        [1, 2, 3],
        [4, 7, 3],
        [4, 7, 3]]])
'''
        
np.concatenate(t1, axis=2)
'''
array([[[1, 2, 3, 1, 2, 3],
        [1, 0, 2, 1, 0, 2],
        [1, 0, 2, 1, 0, 2]],

       [[1, 2, 3, 1, 2, 3],
        [2, 4, 5, 2, 4, 5],
        [2, 4, 5, 2, 4, 5]],

       [[1, 2, 3, 1, 2, 3],
        [2, 2, 7, 2, 2, 7],
        [2, 2, 7, 2, 2, 7]],

       [[1, 2, 3, 1, 2, 3],
        [2, 3, 3, 2, 3, 3],
        [2, 3, 3, 2, 3, 3]],

       [[1, 2, 3, 1, 2, 3],
        [4, 1, 2, 4, 1, 2],
        [4, 1, 2, 4, 1, 2]],

       [[1, 2, 3, 1, 2, 3],
        [4, 7, 3, 4, 7, 3],
        [4, 7, 3, 4, 7, 3]]])
'''


'''Technique to create chunk IDs of consecutive value
Explain: df.value.diff().ne(0) gives a condition True whenever there is a value change. Cumsum gives a non descending 
sequence of groupids where each id denotes a consecutive chunk with same values.
Output:
    id  num  num_groupid
0    1    2            1
1    1    2            1
2    1    3            2
3    1    2            3
4    1    2            3
5    1    2            3
6    1    3            4
7    1    3            4
8    1    3            4
9    1    3            4
10   2    1            5
11   2    4            6
12   2    1            7
13   2    1            7
14   2    1            7
15   2    4            8
16   2    4            8
17   2    1            9
18   2    1            9
19   2    1            9
20   2    1            9
21   2    1            9
'''
#===============================================================================
# data={'id':[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2],
#       'num':[2,2,3,2,2,2,3,3,3,3,1,4,1,1,1,4,4,1,1,1,1,1]}
# df=pd.DataFrame.from_dict(data)
# df['num_groupid'] = df.num.diff().ne(0).cumsum()
#===============================================================================


'''Apply that technique on problem:
identify at the id level (df.groupby['id']) when the value shows the same number consecutively for 3 or more times.
Explain: df.num.diff().ne(0).cumsum() create chunk groupid for `value` as explain above. Next, groupby `id` and this groupid.
    Next, `transform` with `count/size` to assign value to each element of group. Ge(3), astype(int) to convert to bool mask of 1/0
    
desired output:
    id  value  flag
0    1      2     0
1    1      2     0
2    1      3     0
3    1      2     1
4    1      2     1
5    1      2     1
6    1      3     1
7    1      3     1
8    1      3     1
9    1      3     1
10   2      1     0
11   2      4     0
12   2      1     1
13   2      1     1
14   2      1     1
15   2      4     0
16   2      4     0
17   2      1     1
18   2      1     1
19   2      1     1
20   2      1     1
21   2      1     1
'''
#===============================================================================
# data={'id':[1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2],
#       'num':[2,2,3,2,2,2,3,3,3,3,1,4,1,1,1,4,4,1,1,1,1,1]}
# df=pd.DataFrame.from_dict(data)
# df['flag'] = df.num.groupby([df.id, df.num.diff().ne(0).cumsum()]).transform('count').ge(3).astype(int)
#===============================================================================

'''
Pivot examples:
from:
   EMPLOYEE_ID COLORS
0       111111   BLUE
1       222222  GREEN
2       333333    RED
3       333333  GREEN

to:
k           COLOR_1 COLOR_2
EMPLOYEE_ID
111111         BLUE    None
222222        GREEN    None
333333          RED   GREEN
'''
#===============================================================================
# '''Method 1: set_index, unstack'''
# df_new = df.assign(k=(df.groupby('EMPLOYEE_ID').cumcount()+1).astype(str)).set_index(['EMPLOYEE_ID', 'k']).unstack(fill_value='').reset_index()
# df_new.columns = df_new.columns.map('_'.join)
# 
# '''Method 2: pivot_table()'''
# df['k'] = (df.groupby('EMPLOYEE_ID').cumcount() + 1).astype(str)    #without astype to str, columns join failed since it needs str
# df_new = df.pivot_table(index=['EMPLOYEE_ID'], columns=['k'], aggfunc='first', fill_value='')
# ###OR
# df_new = df.pivot_table(index=['EMPLOYEE_ID'], columns=['k'], values=['COLORS'], aggfunc='first',  fill_value='')
# df_new.columns = df_new.columns.map('_'.join)
# 
# '''Method 3: pivot'''
# df['k'] = (df.groupby('EMPLOYEE_ID').cumcount() + 1).astype(str)
# df_new = df.pivot(index='EMPLOYEE_ID', columns='k', values='COLORS').add_prefix('COLORS_') #NO additional columns index added.
# ###OR
# ###In this form, it is exactly same `pivot`. However, fill_value parm help replace None with ''
# df.pivot_table(index='EMPLOYEE_ID', columns='k', values='COLORS', aggfunc='first', fill_value='').add_prefix('COLORS_')
# 
# '''Method 3a: pivot NO add_prefix'''
# df['k'] = (df.groupby('EMPLOYEE_ID').cumcount() + 1).astype(str)
# df_new = df.pivot(index='EMPLOYEE_ID', columns='k') #not specify `values` will add a level making MultiIndex, so need index map
# df_new.columns = df_new.columns.map('_'.join)
# 
# '''Method 4: groupby, first, unstack. Insteresting
# Note: This method unstack from series so final df has single index, while Method 1 unstack from df, so final df has multiindex columns
# !!!'''
# df['k'] = (df.groupby('EMPLOYEE_ID').cumcount() + 1).astype(str)
# df_new = df.groupby(['EMPLOYEE_ID', 'k'])['COLORS'].first().unstack(fill_value='').add_prefix('COLORS_')
#===============================================================================

#===============================================================================
# '''Method 5: crosstab'''
# df['k'] = (df.groupby('EMPLOYEE_ID').cumcount() + 1).astype(str)
# df_new = pd.crosstab(index=df.EMPLOYEE_ID, columns=df.k, values=df.COLORS, aggfunc='first').fillna('').add_prefix('COLORS_')
#===============================================================================

'''One Hot Encode
https://stackoverflow.com/questions/56298815/how-do-i-perform-one-hot-encoding-on-lists-in-a-pandas-column
from:
df = pd.DataFrame(
 {'messageLabels': [['Good', 'Other', 'Bad'],['Bad','Terrible']]}
)

To:
        messageLabels   Bad   Good  Other  Terrible
0  [Good, Other, Bad]  True   True   True     False
1     [Bad, Terrible]  True  False  False      True
'''
#===============================================================================
# '''Method 1'''
# df.join(df.messageLabels.str.join('|').str.get_dummies().astype(bool))
# 
# '''Method 2'''
# df.join(pd.DataFrame([dict.fromkeys(x, True) for x in df.messageLabels]).fillna(False))
# 
# '''Method 3'''
# tmp = pd.DataFrame(df['messageLabels'].tolist())
# df.join(pd.get_dummies(tmp, prefix='', prefix_sep='').max(level=0, axis=1).astype(bool))
# 
# '''Method 4'''
# df.join(pd.get_dummies(tmp, prefix='', prefix_sep='').max(level=0, axis=1).astype(bool))
# 
# '''Method 5'''
# pd.get_dummies(df.messageLabels.apply(lambda x: pd.Series(1, x)) == 1)
#===============================================================================


'''Delete top group of same values
Ex:
ContextID   BacksGas_Flow_sccm  StepID  Time_Elapsed    lof
7308924 1.3671875   25  138.33800000000002              -1
7291161 1.3671875   25  138.767                         -1
7298661 1.3671875   25  121.09500000000001              -1
7313179 1.46484375  25  135.76500000000001               1
7315654 1.5625  25  137.93                               1
7315653 1.5625  25  137.716                              1
7315321 1.5625  25  137.721                              -1
7315320 1.5625  25  137.57600000000002                   -1
'''
#===============================================================================
# '''Method 1:
# Classic solution: create groupID per same value row and ignore groupID# 1'''
# df[df.lof.ne(df.lof.shift()).cumsum() > 1]
# 
# '''Method 2: 
# Specific for this case because of -1 and 1. Eq(1) False on -1, cumsum() create groupID# 0 of top -1, the rest is groupID# NOT 0'''
# df[df.lof.eq(1).cumsum().ne(0)] #instead of ne(0), may use gt(0). because cumsum on series True/False increase from 0
# 
# '''Method 3: shorter!!!
# Specific for this case. Cummax() return all -1 for top group, it turn to 1 for the rest'''
# df[df.lof.cummax().eq(1)]
#===============================================================================


'''Vectorized matrix Euclidean distance in numpy
A = np.array([[1, 2],
     [2, 1]])

B = np.array([[1, 1],
     [2, 2],
     [1, 3],
     [1, 4]])

To:
Out[93]:
array([[1.        , 1.        , 1.        , 2.        ],
       [1.        , 1.        , 2.23606798, 3.16227766]])
'''
'''SO version:'''
# def euclidean_distmtx(X, Y):
#     f = -2 * np.dot(X, Y.T)
#     xsq = np.power(X, 2).sum(axis=1).reshape((-1, 1))
#     ysq = np.power(Y, 2).sum(axis=1)
#     return np.sqrt(xsq + f + ysq)

'''Andy's Euclidean version
a[:,None] is insert new axis after axis=0, so new axis=1 created  and current 1 push to axis=2
So, A[:,None] is 2x1x2 same as A[:,None,:]. B is 4x2, in this equation broadcast to 2x4x2
So, no need B[None,...] to create 1x4x2 which also broadcast to 2x4x2
'''
def euc_dist(a, b):
#     ab_d = a[:,None,:] - b[None,...]    #same as below    
    ab_d_sum = np.power(a[:,None] - b, 2).sum(axis=-1)     
    
    return np.sqrt(ab_d_sum)

def manhattan_dist(a, b):
    return np.abs(a[:,None] - b).sum(-1)

'''A[:,0] (x2), B[:,0](x4) is values of x-axis of points in A and B. A[:,0,None] (2x1) broadcast with B[:,0] create (2x4)'''
def manhattan_dist_fast(a, b):
    return np.abs(A[:,0,None] - B[:,0]) + np.abs(A[:,1,None] - B[:,1])

def chebyshev_dist(a, b):
    pass

A = np.array([[1, 2],
     [2, 1]])

B = np.array([[1, 1],
     [2, 2],
     [1, 3],
     [1, 4]])

print(euc_dist(A,B))
print(manhattan_dist(A,B))    


'''Numpy one-hot encoding
n = array([[1, 1, 2],
       [1, 2, 3]])
       
Out:
array([[[0., 1., 0., 0.],
        [0., 1., 0., 0.],
        [0., 0., 1., 0.]],

       [[0., 1., 0., 0.],
        [0., 0., 1., 0.],
        [0., 0., 0., 1.]]])
'''
'''Method 1: np.eye and fancy index'''
np.eye(4)[n]

'''Method 2: np.arange and broadcasting'''
(np.arange(4) == n[...,None]).astype(int)

'''Method 3: np.zeros and fancy index assignment'''
a = np.zeros((2, 3, 4))
a[np.arange(2)[:,None], np.arange(3)[None,:], n] = 1


