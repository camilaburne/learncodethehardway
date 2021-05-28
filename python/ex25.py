def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This function will sort words for us."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """This function will take a full sentence and return sorted words for us."""
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
    """Prints first and last words of sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Prints first and last sorted words of sentence"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
