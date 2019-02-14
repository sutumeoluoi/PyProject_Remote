'''
Created on Sep 17, 2018

@author: Sutu_MeoLuoi
'''
"""Test the Task data type."""
from collections import namedtuple
from pytest import mark
from time import sleep

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
    'owner': 'okken',
    'done': True,
    'id': 21}
    assert t_dict == expected

@mark.test_these    
def test_replace():
    """replace() should change passed in fields."""
    sleep(1)
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=11, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected