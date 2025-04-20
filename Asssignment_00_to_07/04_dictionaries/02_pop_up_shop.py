def main():
    
    fruits = {
        "apple": 10.5,
        "durian": 25.0,
        "jackfruit": 15.5,
        "kiwi": 8.0,
        "rambutan": 12.5,
        "mango": 9.0
    }

    total = 0  

    for fruit, price in fruits.items():
        quantity = input(f"How many ({fruit}) do you want to buy?: ")
        try:
            quantity = int(quantity)
            total += quantity * price
        except ValueError:
            print(f"Invalid input for {fruit}. Assuming 0.")
    
    print(f"\nYour total is ${total}")

if __name__ == '__main__':
    main()
