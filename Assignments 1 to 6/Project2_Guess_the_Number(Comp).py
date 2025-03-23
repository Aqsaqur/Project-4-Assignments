import random

def Guess(x):
    random_number = random.randint(1, x)
    guess = 0
    lives = 3
    while guess !=random_number and lives:
        guess = int(input(f"Guess the Number between 1 to {x}: "))
        if guess < random_number:
            print("Too Low, Guess Again")
        elif guess > random_number:
            print("Too High, Guess Again")
        lives -= 1
        print(f"Lives remaining: {lives}")
        
    print("Congrats, You have guessed the number ")

Guess(10)

