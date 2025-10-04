import random

# Generate a random number between 1 and 100
match = random.randint(1, 100)

print("Welcome to guess between 1 to hundred:")
num = int(input("Enter number between 1 to 100:"))

# Check if the number is within the valid range
if num < 1 or num > 100:
    print("You are out of required range.")
else:
    print(f"The secret number was: {match}")  # Optional: remove this to keep it secret
    if num > match:
        print("Too high! You lose.")
    elif num < match:
        print("Too low! You lose.")
    else:
        print("Perfect match! You won!")

print("Thanks for playing!!")