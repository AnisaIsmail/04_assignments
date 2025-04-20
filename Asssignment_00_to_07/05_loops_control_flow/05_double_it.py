def main():
    # Ask user for a number and convert it to int
    curr_value = int(input("Enter a number: "))

    # Keep doubling and printing until value is 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=" ")

    print()  # For a clean new line

if __name__ == '__main__':
    main()
