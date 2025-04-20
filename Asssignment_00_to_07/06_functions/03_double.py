def double(num):
    return num * 2

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))

    # Call the double function
    result = double(num)

    # Print the result
    print("Double that is", result)

if __name__ == '__main__':
    main()