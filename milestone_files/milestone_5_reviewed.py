import random
# TODO: Ensure to maintain two lines of space between
# the import statement and the class definition


class Hangman: 
     # TODO: Add a docstring for your class here and include
    # descriptions of your attributes and methods
    def __init__(self,word_list, num_lives):
        # TODO: Add a docstring for your initialiser here
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        # TODO: Try to describe your method in one line.
        # For docstrings, don't try to explain the method 
        # in a great amount of detail, as that is what 
        # comments are used for (the code here is actually 
        # self-explanatory, so you don't need comments). 
        # Also add a description for your guess parameter
        """
        A method which takes in guess then check if the guess letter is in the random chosen word, 
        if so it will then decrease number of letters left to guess in the word and print the remaining letters left to guess; 
        if not it will print that it is not the right letter, decrease number of lives by 1 and print that out too.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index,char in enumerate(list(self.word)):
                if char == guess:
                    self.word_guessed[index] = guess
            self.num_letters -=1
            print(self.word_guessed)
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left.")


    # TODO: Ensure only a single space separates each method
    def ask_for_input(self):
        # TODO: Try to describe your method in one line.
        """
        A method which ask player for input then check
        - if the letter is not an alphabet, if so it will print a warning statement
        - if the letter is in the guess listr, if so it will print a warning statement
        - if the letter is an alphabet and does not appear in the word guessed then
                - run check_guess method 
                - append the list of guesses variable
                - the loop breaks
        """
        while True: 
            guess = input("Please input a letter: ")
            # TODO: Add another clause to this if statement to
            # reject inputs of more than one alphabetical character
            # i.e., 
            # if guess.isalpha() != True or len(guess) != 1:
            if guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
# TODO: Ensure to have two lines of space separating 
# the last line of code belonging to your class and
# first line of your non-class code
def play_game(word_list):
    # TODO: Try to describe your function in one line.
    """
    A function outside the class which will start the game by creating an instance of the Hangman class using
     a variable called game. 
    A while loop is used to continue the game until either 
     - the number of lives becomes 0 
     - the number of letters is 0 
      then break
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True: 
        # TODO: Move the print statement of your
        # game.word_guessed attribute here so that
        # the player sees this for every guess made,
        # not just when the guess is correct.
        if game.num_lives == 0:
            print("You lost")
            break
        elif game.num_letters >0:
            game.ask_for_input()
        else: 
            print("Congratulations. You won the game!")
            break

# TODO: Add an if __name__ == '__main__': here  
# and add the last two lines of code inside it
# TODO: The comment below is not needed
# list to be passed into word_list parameter in Hangman class       
play_game(["mango", "honeydew", "durian", "dragonfruit", "kiwi"])



     

