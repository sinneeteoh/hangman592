import random


class Hangman: 
    """
    A hangman class with a constructor, and 2 methods with a total of 7 attributes.
    """

    def __init__(self,word_list, num_lives):
        """
        A constructor which is automatically called when a new instance of a class is created. 2 attributes are in this constructor.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        A method which takes in guess as an attribute then check if the guess letter is in the randomly chosen word.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index,char in enumerate(list(self.word)):
                if char == guess:
                    self.word_guessed[index] = guess
            self.num_letters -=1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        A method which ask player for input then check if the letter is an alphabet and if it has been previously guessed.
        """
        while True: 
            guess = input("Please input a letter: ")
            if guess.isalpha() != True or len(guess) !=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    A function outside the class which will start the game by creating an instance of the Hangman class using a variable called game. 
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        print(game.word_guessed) 
        if game.num_lives == 0:
            print("You lost")
            break
        elif game.num_letters >0:
            game.ask_for_input()
        else: 
            print("Congratulations. You won the game!")
            break


if __name__ == "__main__":
    print("File",__name__,"is successfully executed.")
    play_game(["mango", "honeydew", "durian", "dragonfruit", "kiwi"])


   




     

