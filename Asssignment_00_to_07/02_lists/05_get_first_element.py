def get_first_element(lst):
    # Print the first element in the list
    print("The first element is:", lst[0])

def main():

    num_elements = int(input("How many elements do you want to enter? "))

    # Create an empty list to store the elements
    user_list = []

    # Get the elements one by one
    for i in range(num_elements):
        element = input(f"Enter element #{i + 1}: ")
        user_list.append(element)

    # Print the full list
    print("Your list:", user_list)

    # Call the function to print the first element
    get_first_element(user_list)

if __name__ == '__main__':
    main()
