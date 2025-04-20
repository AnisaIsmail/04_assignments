def main():
    values = []  # Create an empty list to store the values

    while True:
        user_input = input("Enter a value: ")

        if user_input == "":
            break  # Exit the loop if the input is empty

        values.append(user_input)  # Add the input to the list

    print("Here's the list:", values)

if __name__ == '__main__':
    main()
