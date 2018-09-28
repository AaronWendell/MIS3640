def is_abecedarian_while(word):
    """
    returns True if the letters in a word appear in alphabetical order, performed with a while loop
    (double letters are ok).
    """
    if len(word) == 1:
        return True
    word = word.lower()
    c = 0
    while c < len(word) - 1 :
        if ord(word[c]) <= ord(word[c+1]):
            c += 1
        else:
            return False
    return True


def is_abecedarian_recursive(word):
    """
    returns True if the letters in a word appear in alphabetical order, performed recursively
    (double letters are ok).
    """
    if len(word) == 1:
        return True
    word = word.lower()

    if ord(word[0]) <= ord(word[1]):
        return is_abecedarian_recursive(word[1:])
    else:
        return False


print(is_abecedarian_recursive('ab'))
# print(is_abecedarian('college'))