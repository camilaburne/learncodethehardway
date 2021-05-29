verbs = ('go', 'stop', 'kill', 'eat')
stopw = ('the', 'in', 'of', 'from')
nouns = ('door', 'bear', 'princess')

def scan(words):
    """This function takes a sentence and returns
    a list of tuples with each word categorized"""
    result = []
    word_list = words.split(' ')

    for word in word_list:
        if word in verbs:
            result.append(('verbs', word))
        elif word in nouns:
            result.append(('nouns', word))
        elif word in stopw:
            result.append(('stopw', word))
        else:
            result.append(('not_found', word))
    return result
