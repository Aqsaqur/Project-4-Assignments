def Checking_double():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling until curr_value is 100 or greater
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")  # Print values in the same line
    
    print()  # New line after loop ends


if __name__ == '__main__':
    Checking_double()