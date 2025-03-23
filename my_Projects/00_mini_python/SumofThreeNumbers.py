# Write a program that takes three numbers as input from the user, adds them, and displays the result.

def three_numbers():
     print("This program adds three numbers.")
     num1 = int(input("Enter first number: "))

     num2 = int(input("Enter second number: "))

     num3 = int(input("Enter third nymber: "))

     total_sum : int = num1 + num2 + num3

     print(f"The sum of {num1}, {num2} and {num3} is {total_sum}.")

if __name__ == '__main__':
    three_numbers()


