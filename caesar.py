import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    lowercase = letter.lower()
    return alphabet.index(lowercase)

def rotate_character(char, rot):
    alphabet = string.ascii_lowercase
    alphabet2 = string.ascii_uppercase
    fullalphabet = string.ascii_lowercase + string.ascii_uppercase


    if char.isalpha() == False:

        return char

    else:

        if char.isupper():
            letterindex = alphabet_position(char)
            pos = letterindex + rot
            if pos < 26:
                return alphabet2[pos]
            else:
                return alphabet2[pos % 26]

        else:
            letterindex = alphabet_position(char)
            pos = letterindex + rot
            if pos < 26:
                return alphabet[pos]
            else:
                return alphabet[pos % 26]

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted
