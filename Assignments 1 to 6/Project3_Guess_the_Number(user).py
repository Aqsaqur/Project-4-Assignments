import random

def computer_guess(x):
    print("Welcome to Guess the Number Game where computer will guess your number and  will have 3 lives ")
    low = 1
    high = x
    feedback = '' 
    lives = 3
    while feedback != 'c' and lives > 0:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), or low(L) or correct(C)?').lower
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1

        lives -= 1 # Decrease a life with each attempt
        print(f"Lives remaining: {lives}")

    if feedback == 'c':
        print(f'Congrats! The computer guessed your number, {guess}, correctly!')
    else:
        print("The computer ran out of lives! You win.")


computer_guess(10)
