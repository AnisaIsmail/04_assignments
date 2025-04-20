def main():
    affirmation = "I am capable of doing anything I put my mind to."

    print("Please type the following affirmation:")
    print(affirmation)

    user_input = input()

    # Loop until user types it exactly
    while user_input != affirmation:
        print("Hmmm That was not the affirmation. Please type the following affirmation:")
        print(affirmation)
        user_input = input()

    print("That's right! :)")

if __name__ == '__main__':
    main()
