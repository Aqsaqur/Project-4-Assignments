import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and returns their total."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    return die1, die2, total

def result(num_rolls):
    """Rolls the dice a specified number of times and displays results."""
    die1 = 10  # Local variable to show scope difference
    print(f"die1 starts as: {die1}\n")

    for i in range(num_rolls):
        d1, d2, total = roll_dice()
        print(f"Roll {i+1}: Die 1 = {d1}, Die 2 = {d2}, Total = {total}")

    print(f"\ndie1 is still: {die1} (unchanged outside roll_dice)\n")

if __name__ == '__main__':
    num_rolls = int(input("How many times do you want to roll the dice? "))
    result(num_rolls)

