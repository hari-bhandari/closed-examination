from random import shuffle


def scramble(word):
    if len(word) <= 5:
        return word
    first_two_letters = word[0:2]
    last_two_letters = word[-2:]
    to_be_shuffled_text = list(word[2:-2])
    shuffle(to_be_shuffled_text)
    shuffled_text = ''.join(to_be_shuffled_text)
    return first_two_letters+shuffled_text+last_two_letters


