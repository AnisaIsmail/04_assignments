def sum_list(numbers):
    # Calculate the sum of all numbers in the list
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    # Example list of numbers
    numbers = [1, 2, 3, 4, 5]
    
    # Call the function and print the result
    result = sum_list(numbers)
    print("The sum of the list is:", result)

if __name__ == '__main__':
    main()

