import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice:", total)

def main():
    die1 = 10  # This variable is local to main()
    print("die1 in main() starts as:", die1)
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is still:", die1)

# Call the main function
if __name__ == '__main__':
    main()
