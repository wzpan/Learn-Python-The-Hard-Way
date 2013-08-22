class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, *args):
        # remember we take ('noun','princess') tuples and convert them
        argsnum = len(args)
        if argsnum == 4:
            self.subject = args[0][1]
            self.verb = args[1][1]
            self.num = int(args[2][1])
            self.object = args[3][1]
        elif argsnum == 3:
            self.subject = args[0][1]
            self.verb = args[1][1]
            self.num = 1
            self.object = args[2][1]
        else:
            raise TypeError("__init__() of class Sentence takes 4 or 5 arguments (%d given)" % argsnum )
    
def peek(word_list):
    
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        # notice the pop function here
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        # remove words that belongs to word_type from word_list
        match(word_list, word_type)


class Parser(object):

    def parse_verb(self, word_list):
        skip(word_list, 'stop')
        skip(word_list, 'error')
        skip(word_list, 'stop')
        skip(word_list, 'error')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")

    def parse_num(self, word_list):
        skip(word_list, 'stop')
        skip(word_list, 'error')
        skip(word_list, 'stop')
        skip(word_list, 'error')

        if peek(word_list) == 'number':
            return match(word_list, 'number')
        else:
            return None


    def parse_object(self, word_list):
        skip(word_list, 'stop')
        skip(word_list, 'error')
        skip(word_list, 'stop')
        skip(word_list, 'error')
        next = peek(word_list)

        if next == 'noun':
            return match(word_list, 'noun')
        if next == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")


    def parse_subject(self, word_list, subj):
        verb = self.parse_verb(word_list)
        num = self.parse_num(word_list) # should be placed before object
        obj = self.parse_object(word_list)
        if num is not None:
            return Sentence(subj, verb, num, obj)
        else:
            return Sentence(subj, verb, obj)


    def parse_sentence(self, word_list):
        skip(word_list, 'stop')
        skip(word_list, 'error')
        skip(word_list, 'stop')
        skip(word_list, 'error')

        start = peek(word_list)

        if start == 'noun':
            subj = match(word_list, 'noun')
            return self.parse_subject(word_list, subj)
        elif start == 'verb':
            # assume the subject is the player then
            return self.parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParserError("Must start with subject, object, or verb not: %s" % start)
