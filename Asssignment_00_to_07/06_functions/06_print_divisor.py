def print_divisors(num):
    # Print all divisors of the number 'num'
    print("Here are the divisors of", num)
    
    # Loop from 1 to num to find divisors
    for i in range(1, num + 1):
        if num % i == 0:  # If there's no remainder, i is a divisor
            print(i, end=" ")  # Print the divisor on the same line
    
    print()  
    
def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    print_divisors(num)

if __name__ == '__main__':
    main()
