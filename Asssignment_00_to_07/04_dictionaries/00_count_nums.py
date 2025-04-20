def main():
    counts = {}  # Dictionary to keep track of number counts

    while True:
        entry = input("Enter a number (or press Enter to stop): ")

        if entry == "":
            break

        try:
            num = int(entry)
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        except ValueError:
            print("Please enter a valid number.")

    for num, count in counts.items():
        print(f"{num} appears {count} times.")


if __name__ == '__main__':
    main()
