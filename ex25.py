#Use '' to split each word.
def break_words(stuff):
    """This funcation will break up words for us."""
    words = stuff.split(' ')
    return words

#Sort the words according wo the alphabat.
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#Pop the first word out and print it.
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

#Pop the last word out and print it.
def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)

#Do the first and second function in the meantime.
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
