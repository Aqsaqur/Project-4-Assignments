
INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def unit_measurement():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")
    
    
if __name__ == '__main__':
    unit_measurement()