import random

def main():
    for _ in range(10):
        value = random.randint(1, 100)
        print(value, end=' ')
    print()  # Just to move to a new line after printing all numbers

if __name__ == '__main__':
    main()
