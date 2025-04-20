def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 250,
        "pear": 1000,
        "orange": 300
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip()
    stock = num_in_stock(fruit)
    
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
