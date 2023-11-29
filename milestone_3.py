# Write a code that will continuously ask the user for a letter and validate it
def ask_for_input():
    guess = input("Please input a letter: ")

    while guess.isalpha() != True:
        print("Invalid letter. PLease, enter a single alphabetical character.")
        guess = input("Please input a letter: ")
        
        if guess.isalpha() == True:
            print(guess)
            break

# check whether the guess is in the word

def check_guess(guess):
    guess = guess.lower()
    secret_word =  "apple"

    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    