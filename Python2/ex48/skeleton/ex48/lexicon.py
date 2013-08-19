def scan(line):
    ' scan a line and split into words '
    words = line.split(' ')
    # analyse words
    result = []
    # for each word, send it to the analyzer to analyse
    for word in words:
        type = analyse(word)
        result.append((type, word))
    return result


def analyse(word):
    ''' Input a word, return its type according to the rule.  '''
    rules = {
        "direction": ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
        "verb": ['go', 'stop', 'kill', 'eat'],
        "stop": ['the', 'in', 'of', 'from', 'at', 'it'],
        "noun": ['door', 'bear', 'princess', 'carbinet']
        }
    
    ''' analyse a word '''

    if isnum(word) is not None:
        return 'number'

    for rule, rule_list in rules.items():
        if word in rule_list:
            return rule

    return 'error'

def isnum(word):
    ''' return a int number if is a number, other wise return None '''
    try:
        return int(word)
    except ValueError as er:
        return None
