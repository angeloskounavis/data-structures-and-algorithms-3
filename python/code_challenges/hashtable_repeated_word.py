from data_structures.hashtable import Hashtable
import re


def first_repeated_word(string):
    """
    Find the first repeated word in a string.
    """
    if len(string) < 1:
        return None
    if type(string) is not str:
        raise TypeError
    dict = Hashtable()
    # the following code preprocesses the string into a list of words that ignores punctuation
    # and splits the string on any whitespace
    string = re.sub(r'[^\w\s]', '', string)
    split = re.split(r'[\s]+', string.lower())

    for word in split:
        if dict.get(word):
            return word
        else:
            dict.set(word, True)

    return None
