'''
Created on Sep 9, 2018

@author: Sutu_MeoLuoi
'''
from collections import namedtuple
from pytest import mark


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id']) #Task have no default value. i.e it's None
#__new__ got called on obj creation. __defaults__ hold default values to assign to obj creation 
#when no args pass-in. 
Task.__new__.__defaults__ = (None, None, False, None)   #assign default values through __defaults__ of __new__ 

def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task() #without assign __defaults above, this comment will fail since it require 4 args
    t2 = Task(None, None, False, None)
    assert t1 == t2

@mark.test_these    
def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)