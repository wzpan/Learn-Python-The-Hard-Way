def scan(line):
    ' scan a line and split into words '
    words = line.split(' ')
    # analyse words
    result = []
    # for each word, send it to the analyzer to analyse
    for word in words:
        # Make sure the scanner handles user input in any capitalization and case.
        type = analyse(word.lower())
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
    if word.isdigit():
        # if it's a number
        return 'number'
    for rule, rule_list in rules.items():
        if word in rule_list:
            # if it match any rule above
            return rule
    return 'error'
