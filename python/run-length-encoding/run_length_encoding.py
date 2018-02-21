def decode(string):
    import pdb
    pdb.set_trace()
    decoded_string = ""
    string_nr = ""
    count = 0
    for char in string:
        if char.isdigit():
            string_nr += str(char)
        else:
            if char == " ":
                count = 0
                continue
            decoded_string += str(string_nr)
    pass


def encode(string):
    encoded_string = ""
    count = 0
    last_char = ""
    for char in string:
        if char == last_char:
            count += 1
        else:
            if count == 0:
                count = 1
            elif count == 1:
                encoded_string += str(last_char)
            else:
                encoded_string += str(count) + last_char
                count = 1
        last_char = char

    if count > 1:
        encoded_string += (str(count) + last_char)
    elif count == 1:
        encoded_string += last_char
    return encoded_string
