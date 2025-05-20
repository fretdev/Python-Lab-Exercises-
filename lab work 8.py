'''
Let’s build a guess game. In this game we would have a secret number and then ask the user to Guess the secret number. 
If the user guesses it right before the 5th guess, the user wins and if he doesn’t the user loses the guess. 
'''
secret_number = 23
user_guess = int(input("Guess the secret number: "))
number_of_guesses = 1
max_guesses = 5
while user_guess != secret_number and number_of_guesses < max_guesses:
    if user_guess < secret_number:
        print("Keep Guesing.")
    else:
        print("You've reached the maximum amount of guess.")
    user_guess = int(input("Guess again: "))
    number_of_guesses += 1
    if user_guess == secret_number:
        print("Congratulations! You guessed the secret number.")
else:
    print("Sorry! You've used all your guesses. The secret number was", secret_number)
