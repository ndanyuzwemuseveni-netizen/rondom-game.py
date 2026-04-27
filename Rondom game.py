import random

# Function to play one round of the game
def play_game(max_number):
    # Generate a random number
    secret_number = random.randint(1, max_number)
    
    attempts = 0
    max_attempts = 7

    print("\nI have chosen a number between 1 and", max_number)

    # Loop for up to 7 attempts
    while attempts < max_attempts:
        user_input = input("Enter your guess: ")

        # Check if input is a number
        if not user_input.isdigit():
            print("Please enter a valid number!")
            continue  # Do not count this as an attempt

        guess = int(user_input)
        attempts += 1  # Count valid attempt

        # Compare guess with the secret number
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("Correct! You guessed the number in", attempts, "attempt(s).")
            return  # End the game if correct

        print("Attempts left:", max_attempts - attempts)

    # If player fails after 7 attempts
    print("Game Over! The correct number was", secret_number)


# Main program
max_number = 100  # starting range

while True:
    play_game(max_number)

    # Increase difficulty each round (bonus)
    max_number += 50

    # Ask if player wants to continue
    answer = input("\nDo you want to play again? (yes/no): ").lower()
    if answer != "yes":
        print("Thanks for playing!")
        break