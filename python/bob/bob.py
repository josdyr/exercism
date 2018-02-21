import re


def hey(phrase):
    sentence = list_sentence(phrase)
    # print(sentence)
    # import pdb
    # pdb.set_trace()
    if len(sentence) == 0:
        return "Fine. Be that way!"
    for word in sentence:
        if word.isupper():
            return "Whoa, chill out!"
    if sentence[-1][-1] == "?":
        return "Sure."
    return "Whatever."


def list_sentence(phrase):
    phrase = re.sub(r"[^a-zA-Z?'\d-]", " ", phrase)
    phrase = re.sub(r" '", " ", phrase)
    phrase = re.sub(r"' ", " ", phrase)
    phrase = phrase.split()
    phrase_list = list(phrase)
    return phrase_list
