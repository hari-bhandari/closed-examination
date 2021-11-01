from random import shuffle


def scramble(word):
    """
       scrambles a word when the length is greater than 5

       Args:
           word (string): word that is to be scrambled.

       Returns:
           str: word that is scrambled

       Raises:
           KeyError: Raises an exception.
       """
    if len(word) <= 5:
        return word
    first_two_letters = word[0:2]
    last_two_letters = word[-2:]
    to_be_shuffled_text = list(word[2:-2])
    shuffle(to_be_shuffled_text)
    shuffled_text = ''.join(to_be_shuffled_text)
    return first_two_letters+shuffled_text+last_two_letters


