def Two_Numbers():
    print("This program adds two numbers.")
    num1 : str = input("Enter first number: ") # Prompt the user to enter the first number
    num1 : int = int(num1)

    num2  : str = input("Enter second number: ") # Prompt the user to enter the second number
    num2 : int = int(num2)
    
    # Calculate the sum
    total_sum : int = num1 + num2
    
    print(f"The sum of {num1} and {num2} is {total_sum}.")



if __name__ == '__main__':
    Two_Numbers()
    