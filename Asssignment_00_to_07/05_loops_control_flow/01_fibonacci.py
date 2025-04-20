# Constant for the maximum value in the sequence
MAX_VALUE = 10000

def main():
    # Starting values of the Fibonacci sequence
    a = 0
    b = 1

    # Print the first number
    print(a, end=" ")

    # Loop to generate and print Fibonacci numbers
    while b < MAX_VALUE:
        print(b, end=" ")
        a, b = b, a + b  # Update the last two values

    print()  # For a clean new line after printing


# Required line to run the main function
if __name__ == '__main__':
    main()
