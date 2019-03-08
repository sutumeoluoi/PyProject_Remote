# This requires at least Python 3.6

import time
import statistics
import random
import collections


def f1(seq):  # Raymond Hettinger
    hash_ = {}
    [hash_.__setitem__(x, 1) for x in seq]
    return hash_.keys()

#===============================================================================
# def f2(seq):   # ********* run so SLOWWWWW!!!
#     # order preserving
#     checked = []
#     for e in seq:
#         if e not in checked:
#             checked.append(e)
#     return checked
#===============================================================================

def f3(seq):
    # Not order preserving
    keys = {}
    for e in seq:
        keys[e] = 1
    return keys.keys()

def f4(seq):  # ********** order preserving
    noDupes = []
    [noDupes.append(i) for i in seq if not noDupes.count(i)]
    return noDupes

def f5(seq, idfun=None):  # Alex Martelli ******* order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen:
            continue
        seen[marker] = 1
        result.append(item)
    return result

def f5b(seq, idfun=None):  # Alex Martelli ******* order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        marker = idfun(item)
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker not in seen:
            seen[marker] = 1
            result.append(item)

    return result

# def f6(seq):
#     # Not order preserving
#     return list(Set(seq))

def f7(seq):
    # Not order preserving
    return list(set(seq))

def f8(seq):  # Dave Kirby
    # Order preserving
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]#seen.add(x) add to checking set and return None
                                #need 'not' in front it to make whole 'if' true to put x into the final list
def f9(seq):
    # Not order preserving, even in Py >=3.6
    return {}.fromkeys(seq).keys()

def f10(seq, idfun=None):  # Andrew Dalke
    # Order preserving
    return list(_f10(seq, idfun))

def _f10(seq, idfun=None):
    seen = set()
    if idfun is None:
        for x in seq:
            if x in seen:
                continue
            seen.add(x)
            yield x
    else:
        for x in seq:
            x = idfun(x)
            if x in seen:
                continue
            seen.add(x)
            yield x

def f11(seq):  # f10 but simpler
    # Order preserving
    return list(_f10(seq))

def _f11(seq):
    seen = set()
    for x in seq:
        if x in seen:
            continue
        seen.add(x)
        yield x

### Only work version >= 3.6. due to dict is keep insertion ordrer
#change to OrderedDict to compare all f's
# def f12(seq):
#     # Raymond Hettinger
#     # https://twitter.com/raymondh/status/944125570534621185
#     return list(dict.fromkeys(seq))
def f12(seq):   #slow, but still much better than f2
    return list(collections.OrderedDict.fromkeys(seq)) #list and dict implement in C, so faster OrderedDict


def timing(f, n, a):
    t1 = time.clock()
    for _ in range(n):
        f(a)
    t2 = time.clock()
    return (t2 - t1) * 1000


def getRandomString(length=10, loweronly=1, numbersonly=0,
                    lettersonly=0):
    """ return a very random string """
    _letters = 'abcdefghijklmnopqrstuvwxyz'
    if numbersonly:
        l = list('0123456789')
    elif lettersonly:
        l = list(_letters + _letters.upper())
    else:
        lowercase = _letters+'0123456789'*2
        l = list(lowercase + lowercase.upper())
    random.shuffle(l)
    s = ''.join(l)
    if len(s) < length:
        s = s + getRandomString(loweronly=1)
    s = s[:length]
    if loweronly:
        return s.lower()
    else:
        return s


def run():
    testdata = {}

    for i in range(35):
        k = getRandomString(5, lettersonly=1)
        v = getRandomString(100)
        testdata[k] = v

    # print(f1(list('abracadabra')))
    # print(f3(list('abracadabra')))
    testdata = []

    for i in range(20000):
        testdata.append(getRandomString(3, loweronly=True))

    order_preserving = f4, f5, f5b, f8, f10, f11
    order_preserving = f5, f5b, f8, f10, f11, f12

    not_order_preserving = f1, f3, f7, f9
    testfuncs = order_preserving + not_order_preserving

    for i, f in enumerate(order_preserving):
        if i:
            prev_f = order_preserving[i - 1]
            r1 = prev_f(testdata)
            r2 = f(testdata)
            # print(len(r1), 100 * len(r1) / len(testdata))
            assert r1 == r2, '{} != {}'.format(prev_f, f)

    for i, f in enumerate(not_order_preserving):
        if i:
            prev_f = not_order_preserving[i - 1]
            r1 = prev_f(testdata)
            r2 = f(testdata)
            # print(len(r1))
            assert set(r1) == set(r2), '{} != {}'.format(prev_f, f)

    times = {}

    testfuncs = list(testfuncs)
    for _ in range(10):
        random.shuffle(testfuncs)
        for f in testfuncs:
            if f not in times:
                times[f] = []
            times[f].append(timing(f, 100, testdata))

    results = []
    for f, mss in times.items():
        results.append((
            f,
            f in order_preserving,
            statistics.mean(mss),
            statistics.median(mss),
        ))

    print(
        'FUNCTION'.ljust(15),
        'ORDER PRESERVING'.ljust(20),
        'MEAN'.ljust(10),
        'MEDIAN',
    )
    results.sort(key=lambda x: (not x[1], x[2]))
    # results.sort(key=lambda x: x[0].__name__)
    for f, is_order_preserving, mean, median in results:
        print(
            f.__name__.ljust(15),
            ('yes' if is_order_preserving else 'no').ljust(20),
            '{:.1f}'.format(mean).ljust(10),
            '{:.1f}'.format(median),
        )


if __name__ == '__main__':
    run()
'''        
********** RESULT ***********
FUNCTION        ORDER PRESERVING     MEAN       MEDIAN
f8              yes                  418.0      414.8
f11             yes                  484.5      482.8
f10             yes                  498.1      482.3
f5b             yes                  838.5      817.3
f5              yes                  850.4      836.4
f12             yes                  4867.3     4815.3
f2              yes                  389097.3   387661.7
f7              no                   149.7      145.5
f9              no                   176.6      171.0
f3              no                   259.3      247.1
f1              no                   611.8      585.4
'''
