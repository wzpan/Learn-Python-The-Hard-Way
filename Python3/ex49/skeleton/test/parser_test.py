from nose.tools import *
from ex49.parser import *

def test_peek():
    ''' test peek function '''
    list1 = [('direction', 'south')]
    assert_equal(peek(list1), 'direction')
    list2 = [('stop', 'the'), ('verb', 'stop')]
    assert_equal(peek(list2), 'stop')
    # test an empty list
    list3 = []
    assert_equal(peek(list3), None)

def test_match():
    ''' test match function '''

