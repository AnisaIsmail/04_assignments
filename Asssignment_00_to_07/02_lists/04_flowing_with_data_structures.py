def add_three_copies(my_list, data):
    # Add three copies of the data to the list
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    
    data = input("Enter a message to copy: ")

    # Create an empty list
    messages = []

    print("\nList before:", messages)

    add_three_copies(messages, data)

    print("List after:", messages)
\
if __name__ == '__main__':
    main()
