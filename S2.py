def sort_numbers():
    # Input list of numbers
    numbers = input("Enter a list of numbers separated by spaces: ")
    
    # Convert the input string into a list of numbers
    try:
        number_list = list(map(float, numbers.split()))
    except ValueError:
        print("Please enter valid numbers.")
        return

    # Ask for the sorting order
    order = input("Enter 'asc' for ascending or 'desc' for descending order: ").strip().lower()

    if order == 'asc':
        sorted_list = sorted(number_list)
    elif order == 'desc':
        sorted_list = sorted(number_list, reverse=True)
    else:
        print("Invalid choice. Please enter 'asc' or 'desc'.")
        return

    # Print the sorted list
    print("Sorted list:", sorted_list)

# Call the function to execute the program
if __name__ == "__main__":
    sort_numbers()
