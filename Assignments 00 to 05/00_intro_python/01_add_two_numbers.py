def Two_Numbers():
    print("This program adds two numbers.")
    num1 : str = input("Enter first number: ") # Prompt the user to enter the first number
    num1 : int = int(num1) # Reading the input and converting it to an integer.

    num2  : str = input("Enter second number: ") # Prompt the user to enter the second number
    num2 : int = int(num2) # Reading the input and converting it to an integer.
    
    # Calculate the sum
    total_sum : int = num1 + num2
    
    print(f"The sum of {num1} and {num2} is {total_sum}.")


# Main program execution
if __name__ == '__main__':
    Two_Numbers()
    

"""This code in Pseudo-Code 

FUNCTION Two_Numbers():
    PRINT "This program adds two numbers."

    // Prompt the user to enter the first number
    DISPLAY "Enter first number: "
    num1 ← READ INPUT AS STRING
    num1 ← CONVERT num1 TO INTEGER

    // Prompt the user to enter the second number
    DISPLAY "Enter second number: "
    num2 ← READ INPUT AS STRING
    num2 ← CONVERT num2 TO INTEGER

    // Calculate the sum
    total_sum ← num1 + num2

    // Display the result
    DISPLAY "The sum of", num1, "and", num2, "is", total_sum

END FUNCTION

// Main program execution
IF main program is running THEN
    CALL Two_Numbers()
END IF

"""

