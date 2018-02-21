import string


def is_pangram(sentence):
    sentence = set(sentence.lower())
    alphabet = set(string.ascii_lowercase)
    # check if alphabet is a subset of sentence
    if alphabet < sentence:
        return True
    else:
        return False
