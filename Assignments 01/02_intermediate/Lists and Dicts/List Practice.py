def main():
    # Create a list called fruit_list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated list:", fruit_list)

# Run the function
main()

def access_element(lst, index):
    """Returns the element at the specified index, or an error message if out of range."""
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range!"

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with a new value."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    return "Index out of range!"

def slice_list(lst, start, end):
    """Returns a slice of the list within the given index range."""
    if 0 <= start < len(lst) and 0 < end <= len(lst) and start < end:
        return lst[start:end]
    return "Invalid slice range!"

def index_game():
    """Text-based interactive game for list operations."""
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    while True:
        print("\nAvailable operations:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Choose an operation (1-4): ")

        if choice == '1':  # Access element
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == '2':  # Modify element
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':  # Slice list
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))

        elif choice == '4':  # Exit
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the game
index_game()

