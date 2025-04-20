def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

# Function to modify element at index
def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Updated list: {my_list}"
    else:
        return "Index out of range."

# Function to slice the list
def slice_list(my_list, start, end):
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list) and start < end:
        return my_list[start:end]
    else:
        return "Invalid slice indices."

# Game function for interaction
def index_game():
    # Sample list
    my_list = ['dog', 'cat', 'fish', 'rabbit', 'parrot']

    while True:
        print("\nList:", my_list)
        print("Choose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Element:", access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

index_game()