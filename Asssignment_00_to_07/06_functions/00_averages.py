def average(num1, num2):
    # Calculate average of two numbers
    return (num1 + num2) / 2


def main():
    # Ask user for two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Call the average function
    result = average(number1, number2)

    # Print the result
    print("The average is:", result)

if __name__ == '__main__':
    main()
