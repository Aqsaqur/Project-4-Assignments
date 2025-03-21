import random

def random_number():
    # Generate and print 10 random numbers in the range 1 to 100
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
    print()  # Move to the next line after printing all numbers

if __name__ == '__main__':
    random_number()
