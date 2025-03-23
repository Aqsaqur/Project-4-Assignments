"""Ask the user for the length and width of a rectangle and calculate its area.

Formula: area = length * width"""

def calculate_rectangle_area():
    print("Rectangle Area Calculator")
    
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = length * width
    
    print(f"The area of the rectangle is: {area}")

calculate_rectangle_area()

