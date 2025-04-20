import math

def main():
    # Get the lengths of the two sides from the user
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()
