from nose.tools import *
from ex48 import lexicon


def text_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east west down up left right back")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'eat'),
                          ('direction', 'west'),
                          ('direction', 'down'),
                          ('direction', 'up'),
                          ('direction', 'left'),
                          ('direction', 'right'),
                          ('direction', 'back')
                          ])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat stop")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat'),
                          ('verb', 'stop')
                          ])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of from at it")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of'),
                          ('stop', 'from'),
                          ('stop', 'at'),
                          ('stop', 'it'),
                          ])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', '1234')])
    result = lexicon.scan("3 91234 23098 8128 0")
    assert_equal(result, [('number', '3'),
                          ('number', '91234'),
                          ('number', '23098'),
                          ('number', '8128'),
                          ('number', '0'),
                          ])


def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error', 'IAS'),
                          ('noun', 'princess')
                          ])
