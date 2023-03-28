import copy
import random

LETTER_POOL = {
    'A': 9,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 3,
    'H': 2,
    'I': 9,
    'J': 1,
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 8,
    'P': 2,
    'Q': 1,
    'R': 6,
    'S': 4,
    'T': 6,
    'U': 4,
    'V': 2,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1
}

LETTER_VALUES = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 2,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

# create a function that will draw 10 letters from the letter pool
def draw_letters():
    # create a copy of the letter pool so we can modify it
    letter_pool_copy = copy.deepcopy(LETTER_POOL)
    # create an empty list to hold the letters for the users hand
    letters = []

    # while the length of the letters list is less than 10
    while len(letters) < 10:
        # create a list of the letters from the letter pool keys
        # and a list of the weights from the letter pool values
        # save the list of letters and the list of weights to variables
        letters_list = list(LETTER_POOL.keys())
        letter_weights = list(LETTER_POOL.values())

        # create a random letter from the letter pool
        # use random.choices to get a random letter from the list of letters
        # first argument is the list of letters
        # second argument is the list of weights
        # third argument is the number of items to return
        # the [0] at the end is to get the first item from the list of letters
        letter = random.choices(letters_list, weights = letter_weights, k = 1)[0]      
        # if the value of the letter in the letter pool is greater than 0
        # ensure that we don't get a negative number
        if letter_pool_copy[letter] > 0:
            # add the letter to the list of letters
            letters.append(letter)
            # subtract 1 from the value of the letter in the letter pool
            # so we decrease the number of times we can get that letter
            letter_pool_copy[letter] -= 1
    print(letters)

    return letters

# check if the users letters from their word are in the letter pool
def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.deepcopy(letter_bank)

    # for each letter in the word check if it is in the letter bank, remove it so we can check the next letter
    # upper case the word so we can compare it to the letter bank
    for letter in word.upper():
        # if the letter is in the letter bank
        if letter in letter_bank_copy:
            # remove the letter from the letter bank
            letter_bank_copy.remove(letter)
        else:
            # this will run if the letter is not in the letter bank
            # if the letter is not in the letter bank the word is not valid
            # if there is a letter in the word that is not present in the `letter_bank` or has too much of compared to the `letter_bank` 
            return False

    # if we get to this point the word is valid
    return True

# calculate the score of the word
def score_word(word):
    score = 0
    for letter in word:
        score += LETTER_VALUES[letter.upper()]

    if len(word) > 6 and len(word) < 11:
        score += 8

    return score

# find the highest scoring word
def get_highest_word_score(word_list):
    # create a tuple to hold the highest scoring word and the score
    # default the highest scoring word to the first word in the list and the score to 0
    highest = (word_list[0],0)
    
    # loop through the list of letters
    for word in word_list:
        # get the score of the word using the score_word function
        score = score_word(word)
        # if the score is greater than the highest score (the second item in the tuple)
        if score > highest[1]:
            # set the highest score to the score of the current word
            highest = (word, score)
        # if the score is equal to the highest score
        # case of tie in scores, use these tie-breaking rules
        elif score == highest[1]:
            # check if the length of the current word is 10
            if len(highest[0]) == 10:
                pass
            # check if the length of the current word is 10 and the length of the highest word is not 10
            elif len(word) == 10 and len(highest[0]) != 10:
                # set the highest word to the current word
                highest = (word, score)
            # check if the length of the current word is less than the length of the highest word
            elif len(word) < len(highest[0]):
                # set the highest word to the current word
                highest = (word, score)

    return highest