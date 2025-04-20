import random

def main():
    # Randomly pick a number between 0 and 99
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    # Ask for the user's first guess
    guess = int(input("Enter a guess: "))

    # Loop until the user guesses correctly
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        
        # Ask for a new guess
        guess = int(input("Enter a new number: "))
    
    # If guess is correct
    print(f"Congrats! The number was: {secret_number}")
            

if __name__ == '__main__':
    main()
