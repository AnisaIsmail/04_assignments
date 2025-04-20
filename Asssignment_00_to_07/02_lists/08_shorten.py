MAX_LENGTH = 3  # Target length of the list

def shorten(lst):
    # Remove elements from the end until the list is MAX_LENGTH long
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(removed_item)

def main():
    lst = []  # Empty list to store user input

    # Prompt the user to enter values
    print("Enter values for the list (press Enter without typing to finish):")
    while True:
        item = input("Enter a value: ")
        if item == "":
            break
        lst.append(item)

    print("\nOriginal list:", lst)

    # Call the shorten function
    shorten(lst)

    print("Modified list:", lst)

if __name__ == '__main__':
    main()
