import random

# Constants
NUM_ROUNDS = 5

# Introduction
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Initialize score
score = 0

# Loop through the rounds
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    # Generate random numbers
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    # Show user their number
    print(f"Your number is {user_number}")
    
    # Get user guess with input validation
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either 'higher' or 'lower': ").lower()
    
    # Game logic
    correct = False
    if guess == "higher" and user_number > computer_number:
        correct = True
    elif guess == "lower" and user_number < computer_number:
        correct = True
    
    # Outcome
    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    
    # Print score
    print(f"Your score is now {score}\n")

# Game end
print("Thanks for playing!")

# Ending message based on performance
if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")