def in_range(n, low, high):
    """ Returns True if n is between low and high, inclusive. """
    return low <= n <= high

def main():
    n = int(input("Enter the number (n): "))
    low = int(input("Enter the lower bound (low): "))
    high = int(input("Enter the upper bound (high): "))

    result = in_range(n, low, high)
    print(result)

if __name__ == '__main__':
    main()
