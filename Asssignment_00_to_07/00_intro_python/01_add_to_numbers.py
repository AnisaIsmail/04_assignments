def main():
    num1 = input("Enter the first number: ")
    num1 = int(num1)
    num2 = input("Enter the second number: ")
    num2 = int(num2)

    Total = num1 + num2
    print(f"The sum of the two numbers is: {Total}")

# The following block should be outside of the main() function
if __name__ == '__main__':
    main()