def check_number():
    # Take input from the user
    num = float(input("Enter a number: "))

    # Check conditions and print the result
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

# Run the function
if __name__ == '__main__':
    check_number()



