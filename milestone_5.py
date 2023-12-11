import random

class Hangman: 

    def __init__(self,word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index,char in enumerate(list(self.word)):
                if char == guess:
                    self.word_guessed[index] = guess
                    print(self.word_guessed)
                else: 
                    self.num_lives -=1
                    print(f"Sorry,{guess} is not in the word.")
                    print(f"You have {self.num_lives} lives left.")
            self.num_letters -=1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")


    def ask_for_input(self):
        while True: 
            guess = input("Please input a letter: ")
            if guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True: 
        if num_lives == 0:
            print("You lost")
        elif num_lives >0:
            game.ask_for_input()
        else: 
            print("Congratulations. You won the game!")
    
        
play_game(["mango", "honeydew", "durian", "dragonfruit", "kiwi"])



     

