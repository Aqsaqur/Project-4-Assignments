def Fahrenheit_to_celsius():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    Fahrenheit_to_celsius()
    
"""pseudocode for your Fahrenheit to Celsius conversion program:
FUNCTION Fahrenheit_to_celsius():
    // Prompt the user for temperature in Fahrenheit
    DISPLAY "Enter temperature in Fahrenheit: "
    fahrenheit ← READ INPUT AS FLOAT

    // Convert to Celsius using the formula
    celsius ← (fahrenheit - 32) * 5.0 / 9.0

    // Print the result
    DISPLAY "Temperature: ", fahrenheit, "F = ", celsius, "C"
END FUNCTION

// Main program execution
IF main program is running THEN
    CALL Fahrenheit_to_celsius()
END IF
"""