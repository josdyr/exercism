def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1:
            if letter == " " or letter == "-":
                continue
            return False
    return True
