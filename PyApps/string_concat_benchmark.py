import perfplot
import pandas as pd
import numpy as np

def brenbarn(df):
    return df.assign(baz=df.bar.map(str) + " is " + df.foo)

def danielvelkov(df):
    return df.assign(baz=df.apply(
        lambda x:'%s is %s' % (x['bar'],x['foo']),axis=1))

def chrimuelle(df):
    return df.assign(
        baz=df['bar'].astype(str).str.cat(df['foo'].values, sep=' is '))

def vladimiryashin(df):
    return df.assign(baz=df.astype(str).apply(lambda x: ' is '.join(x), axis=1))

def erickfis(df):
    return df.assign(
#         baz=df.apply(lambda x: f"{x['bar']} is {x['foo']}", axis=1))    
        baz=df.apply(lambda x: ' is '.join(map(str, x)), axis=1))

def cs1_format(df):
    return df.assign(baz=df.agg('{0[bar]} is {0[foo]}'.format, axis=1))

def cs1_fstrings(df):
#     return df.assign(baz=df.agg(lambda x: f"{x['bar']} is {x['foo']}", axis=1))
    return df.assign(baz=df.agg(lambda x: ' is '.join(map(str, x)), axis=1))

def cs2(df):
    a = np.char.array(df['bar'].values)
    b = np.char.array(df['foo'].values)

    return df.assign(baz=(a + b' is ' + b).astype(str))

def cs3(df):
    return df.assign(
        baz=[str(x) + ' is ' + y for x, y in zip(df['bar'], df['foo'])])
        
data = {'bar': {0: 1, 1: 2, 2: 3}, 'foo': {0: 'a', 1: 'b', 2: 'c'}}
df_ = pd.DataFrame(data)

perfplot.show(
    setup=lambda n: pd.concat([df_] * n, ignore_index=True),
    kernels=[
        brenbarn, danielvelkov, chrimuelle, vladimiryashin, erickfis, 
        cs1_format, cs1_fstrings, cs2, cs3
    ],
    labels=[
        'brenbarn', 'danielvelkov', 'chrimuelle', 'vladimiryashin', 'erickfis', 
        'cs1_format', 'cs1_fstrings', 'cs2', 'cs3'
    ],
    n_range=[2**k for k in range(0, 8)],
    xlabel='N (x len(df_))',    
    logx=True,
    logy=True,
    equality_check=lambda x, y: (x == y).values.all())
