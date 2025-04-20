def get_last_element(lst):
    # Print the last element in the list
    print("The last element is:", lst[-1])  # Using negative index to get the last item

def main():
    
    num_elements = int(input("How many elements do you want to enter? "))

    user_list = []

    # Collect user inputs
    for i in range(num_elements):
        element = input(f"Enter element #{i + 1}: ")
        user_list.append(element)

    # Show the full list
    print("Your list:", user_list)

    # Print the last element
    get_last_element(user_list)

if __name__ == '__main__':
    main()
