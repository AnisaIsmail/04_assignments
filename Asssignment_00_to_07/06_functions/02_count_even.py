def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print("Number of even numbers:", count)


def main():
    lst = []

    # Keep asking the user until they press Enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Stop if Enter is pressed
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("That's not a valid integer. Try again.")

    # Call the count_even function
    count_even(lst)


# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
