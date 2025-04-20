def main():
    # Prompt the user to enter a number of feet
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * 12

    print(f"{feet} foot is {inches} inches." if feet == 1 else f"{feet} feet is {inches} inches.")

if __name__ == '__main__':
    main()
