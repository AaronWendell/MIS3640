fin = open("session09/words.txt")
# line = fin.readline()
# word = line.strip()
# print(word)

# counter = 0
# for line in fin:
#     word = line.strip()
#     counter += 1
#     # print(word)
# print(counter)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    fin = open('session09/words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))

# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it
    """
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True
    # return not 'e' in word.lower()

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA'))


def find_words_no_e():
    fin = open('words.txt')
    counter_no_e = 0
    counter_total = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if has_no_e(word):
            # print(word)
            counter_no_e += 1
    return counter_no_e/counter_total

# print('The percentage of the words with no "e" is {:.2f}%.'.format(find_words_no_e()*100))


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

# print(avoids('Babson', 'e'))
# print(avoids('College', 'e'))


def find_words_no_vowels():
    fin = open('session09/words.txt')
    counter_no_vowel = 0
    counter_total = 0
    for line in fin:
        counter_total += 1
        word = line.strip()
        if avoids(word, 'aeiouy'):
            print(word)
            counter_no_vowel += 1
    return counter_no_vowel/counter_total


print('The percentage of the words with vowel letters is {:.2f}%.'.format(
    find_words_no_vowels()*100))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def find_words_only_using_planet():
    fin = open('session09/words.txt')
    number_of_words_using_planet = 0
    for line in fin:
        word = line.strip()
        if uses_only(word, 'planet'):
            print(word)
            number_of_words_using_planet += 1
    return number_of_words_using_planet


print('Number of words using only letters from "planet":',
      find_words_only_using_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True
    return uses_only(required, word)


print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


def find_words_using_all_vowels():
    fin = open("Session 09/words.txt")
    counter = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, 'aeiouy'):
            counter += 1
    return counter

find_words_using_all_vowels()


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    before = word[0]
    for letter in word:
        if letter < before:
            return False
        before = letter
    return True


print(is_abecedarian('abs'))
print(is_abecedarian('college'))


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <= 1:
        return True
    if word[0] > word[0]:
        return False
    return is_abecedarian_using_recursion(word[1:])


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i:]:
            return False
        i = i + 1
    return True
