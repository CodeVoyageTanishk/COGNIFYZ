import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've chosen a number between 1 and 20. You have 5 attempts to guess it.")

    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0

    while attempts < 5:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number!")
            break
        
        attempts += 1
        remaining_attempts = 5 - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts left.")
        else:
            print("Sorry, you've run out of attempts. The correct number was", secret_number)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guessing_game()
    else:
        print("Thank you for playing!")

# Start the game
guessing_game()
