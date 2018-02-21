import re


def word_count(phrase):
    phrase = phrase.lower()
    phrase = re.sub(r"[^a-zA-Z'\d]", " ", phrase)
    phrase = re.sub(r" '", " ", phrase)
    phrase = re.sub(r"' ", " ", phrase)
    phrase = phrase.split()
    phrase_list = {}
    for word in phrase:
        if word not in phrase_list:
            phrase_list.update({word: 1})
        else:
            phrase_list[word] += 1
    return phrase_list
