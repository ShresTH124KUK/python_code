import random

class NumberGuessingGame:
    def __init__(self, min_num, max_num, max_attempts):
        self.min_num = min_num
        self.max_num = max_num
        self.secret_number = random.randint(min_num, max_num)
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts

    def guess(self, num):
        if num < self.min_num or num > self.max_num:
            raise ValueError(f"Number must be between {self.min_num} and {self.max_num}")
        
        self.attempts_left -= 1

        if num == self.secret_number:
            return "Congratulations! You guessed the number!"
        elif num < self.secret_number:
            return "Too low! Try a higher number."
        else:
            return "Too high! Try a lower number."

    def get_attempts_left(self):
        return self.attempts_left

def play_game():
    min_num = 1
    max_num = 100
    max_attempts = 5

    game = NumberGuessingGame(min_num, max_num, max_attempts)
    print("Welcome to the Number Guessing Game!")
    print(f"Guess the secret number between {min_num} and {max_num}.")

    while game.get_attempts_left() > 0:
        try:
            guess = int(input("Enter your guess: "))
            result = game.guess(guess)
            print(result)
            if result.startswith("Congratulations"):
                break
        except ValueError as e:
            print(e)

    if game.get_attempts_left() == 0:
        print(f"Sorry, you ran out of attempts. The secret number was {game.secret_number}.")

play_game()
