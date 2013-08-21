from nose.tools import *
from ex49.parser import *
from copy import deepcopy


# construct a test set that consists of several test lists
global_test_lists = [[('direction', 'south')],
                     [('noun', 'door')],
                     [('verb', 'go')],
                     [('stop', 'to')],
                     [('number', '234')],
                     [('error', 'r2d2')],
                     [('stop', 'the'), ('direction', 'east'), ('noun', 'door')],
                     [('verb', 'go'), ('stop', 'to'), ('direction', 'east')],
                     [('noun', 'bear'), ('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'door')],
                     [('stop', 'the'), ('noun', 'princess'), ('verb', 'kill'), ('stop', '10'), ('noun', 'bear')],
                     []
                    ]

# the type of the the first tuple for each test list
test_types = ['direction', 'noun', 'verb', 'stop', 'number', 'error',
               'stop', 'verb', 'noun', 'stop', None]

list_len = len(global_test_lists)


def test_peek():
    ''' test peek function '''
    test_lists = deepcopy(global_test_lists)
    for i in range(list_len):
        test_list = test_lists[i]
        expected_word = test_types[i]
        assert_equal(peek(test_list), expected_word)


def test_match():
    ''' test match function '''
    test_lists = deepcopy(global_test_lists)
    for i in range(list_len):
        test_list = test_lists[i]
        test_type = test_types[i]
        if len(test_list) > 0:
            expected_tuple = test_list[0]
        else:
            expected_tuple = None
        assert_equal(match(test_list, test_type), expected_tuple)



def test_skip():
    ''' test skip function '''
    test_lists = deepcopy(global_test_lists)
    expected_lists1 = [[('direction', 'south')],
                    [('noun', 'door')],
                    [('verb', 'go')],
                    [],
                    [('number', '234')],
                    [('error', 'r2d2')],
                    [('direction', 'east'), ('noun', 'door')],
                    [('verb', 'go'), ('stop', 'to'), ('direction', 'east')],
                    [('noun', 'bear'), ('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'door')],
                    [('noun', 'princess'), ('verb', 'kill'), ('stop', '10'), ('noun', 'bear')],
                    []
                  ]

    for i in range(list_len):
        test_list = test_lists[i]
        expected_list = expected_lists1[i]
        skip(test_list, 'stop')
        assert_equal(test_list, expected_list)


def test_parse_verb():
    ''' test parse_verb function '''

    # test good situations
    test_lists_good =  [[('verb', 'go')],
                        [('verb', 'go'), ('stop', 'to'), ('direction', 'east')],
                        [('stop', 'to'), ('verb', 'eat')]
                       ] 
    
    expected_lists = [('verb', 'go'), ('verb', 'go'), ('verb', 'eat')]
        
    for i in range(len(test_lists_good)):
        test_list = test_lists_good[i]
        expected_list = expected_lists[i]
        assert_equal(parse_verb(test_list), expected_list)
    
    # test bad situations
    test_lists_bad = [[('direction', 'south')],
                     [('noun', 'door')],
                     [('stop', 'to')],
                     [('number', '234')],
                     [('error', 'r2d2')],
                     [('direction', 'east'), ('noun', 'door')],
                     [('noun', 'bear'), ('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'door')],
                     [('stop', 'the'), ('noun', 'princess'), ('verb', 'kill'), ('stop', '10'), ('noun', 'bear')],
                     []
                    ]
    for i in range(len(test_lists_bad)):
        test_list = test_lists_bad[i]
        with assert_raises(ParserError) as cm:
            parse_verb(test_list)
        assert_equal(str(cm.exception), "Expected a verb next.")


def test_parse_object():
    ''' test parse_object function '''
    
    # test good situations
    test_lists_good =  [[('direction', 'south')],
                        [('noun', 'door')],
                        [('stop', 'the'), ('noun', 'bear')],
                        [('direction', 'east'), ('noun', 'door')],
                        [('noun', 'bear'), ('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'door')],
                        [('stop', 'the'), ('noun', 'princess'), ('verb', 'kill'), ('stop', '10'), ('noun', 'bear')],
                       ] 
    
    expected_lists = [('direction', 'south'), ('noun', 'door'), ('noun', 'bear'),
                    ('direction', 'east'), ('noun', 'bear'), ('noun', 'princess')]
        
    for i in range(len(test_lists_good)):
        test_list = test_lists_good[i]
        expected_list = expected_lists[i]
        assert_equal(parse_object(test_list), expected_list)
    
    # test bad situations
    test_lists_bad = [[('verb', 'go')],                      
                      [('stop', 'to')],
                      [('number', '234')],
                      [('error', 'r2d2')],                      
                      [('verb', 'go'), ('stop', 'to'), ('direction', 'east')],                             []
                    ]
    for i in range(len(test_lists_bad)):
        test_list = test_lists_bad[i]
        with assert_raises(ParserError) as cm:
            parse_object(test_list)
        assert_equal(str(cm.exception), "Expected a noun or direction next.")


def test_class_sentence():

    # test good situations
    test_lists_good =  [[('noun', 'bear'), ('verb', 'go'), ('direction', 'east')],
                        [('noun', 'princess'), ('verb', 'kill'), ('noun', 'bear')],
                       ] 

    for i in range(len(test_lists_good)):
        test_list = test_lists_good[i]
        sentence = Sentence(*test_list)
        assert_equal(sentence.subject, test_list[0][1])
        assert_equal(sentence.verb, test_list[1][1])
        assert_equal(sentence.object, test_list[2][1])

    # test bad situations, for more restrict checking
    # test_lists_bad =  [[('direction', 'south')],
    #                     [('noun', 'bear'), ('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'door')],
    #                     [('stop', 'the'), ('noun', 'princess'), ('verb', 'kill'), ('stop', '10'), ('noun', 'bear')],
    #                     [],                        
    #                    ] 

    # for i in range(len(test_lists_good)):
    #     test_list = test_lists_bad[i]
    #     with assert_raises(TypeError) as cm:
    #         sentence = Sentence(*test_list)
    #     assert_equal(str(cm.exception), "__init__() takes exactly 4 arguments (%d given)" % (len(test_list) + 1))
        

def test_parse_subject():
    ''' test parse_subject function '''
    
    test_lists =  [[('verb', 'eat'), ('noun', 'princess')],
                        [('verb', 'go'), ('stop', 'to'), ('direction', 'east')],
                        [('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'carbinet'), ('noun', 'door')],
                        [('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')]
                       ]

    test_subjects = [('noun', 'bear'), ('noun', 'princess'), ('noun', 'carbinet'), ('noun', 'princess')]
    test_verbs = ['eat', 'go', 'go', 'kill']
    test_objects = ['princess', 'east', 'carbinet', 'bear']

    for i in range(len(test_lists)):
        test_list = test_lists[i]
        test_subject = test_subjects[i]
        test_verb = test_verbs[i]
        test_object = test_objects[i]
        sentence = parse_subject(test_list, test_subject)
        assert_equal(sentence.subject, test_subject[1])
        assert_equal(sentence.verb, test_verb)
        assert_equal(sentence.object, test_object)


def test_parse_sentence():
    ''' test parse_sentence function '''
    
    # test good situations
    test_lists1 =  [
                    [('noun', 'bear'), ('verb', 'go'), ('stop', 'to'), ('stop', 'the'), ('noun', 'door')],
                    [('stop', 'the'), ('noun', 'princess'), ('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')],
                    [('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')]
                   ]

    expected_subjects = ['bear', 'princess', 'player']
    expected_verbs = ['go', 'kill', 'kill']
    expected_objects = ['door', 'bear', 'bear']
        
    for i in range(len(test_lists1)):
        test_list = test_lists1[i]
        sentence = parse_sentence(test_list)
        expected_subject = expected_subjects[i]
        expected_verb = expected_verbs[i]
        expected_object = expected_objects[i]
        assert_equal(sentence.subject, expected_subject)
        assert_equal(sentence.verb, expected_verb)
        assert_equal(sentence.object, expected_object)

    # test bad situations
    test_lists2 =  [
                    [('number', '234')],
                    [('error', 'r2d2')],
                   ]
    for i in range(len(test_lists2)):
        test_list = test_lists2[i]
        with assert_raises(ParserError) as cm:
            sentence = parse_sentence(test_list)
        assert_equal(str(cm.exception), "Must start with subject, object, or verb not: %s" % test_list[0][0])
