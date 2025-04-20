def main():
    MIN_HEIGHT = 50  # Minimum height requirement
    
    while True:
        height_input = input("How tall are you? ")

        if height_input == "":
            print("Goodbye!")
            break  # Exit the loop if user enters nothing

        try:
            height = float(height_input)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == '__main__':
    main()
