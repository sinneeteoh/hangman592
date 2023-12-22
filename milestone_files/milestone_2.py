# This file contains the code for the first milestone
## randomly select a word from the list
import random
word_list = ["mango", "honeydew", "durian", "dragonfruit", "kiwi"]
word = random.choice(word_list)
print(word)

## ask user for input
guess = input("Please add 1 letter: ")

## check that input is a single and an alphabetic character
if len(guess) == 1 and guess.isnumeric() == False:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")