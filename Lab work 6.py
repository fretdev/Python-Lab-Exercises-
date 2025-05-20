# QUESTIONS
# Build a quiz game, Ask the user questions and check if the users answer is same as your answer
# (based on what you have learnt so far)

# SOLUTIONS
while True:
    which_of_these_is_an_arithmetic_operator = input(
        "Which of these is an arithmetic operator? +, not, and, ==: ")
    if which_of_these_is_an_arithmetic_operator not in ["+", "not", "and", "=="]:
        print("Invalid input. Please enter one of the options.")
        continue

    if which_of_these_is_an_arithmetic_operator == "+":
        print("Correct! + is an arithmetic operator.")
        break
    else:
        print("Incorrect!.")
        try_again = input(
            "Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        print("Goodbye!")
        exit()
while True:
    which_of_these_is_symbol_is_used_to_join_two_strings = input(
        "Which of these symbol is used to join two strings? +, *, /, %: ")
    if which_of_these_is_symbol_is_used_to_join_two_strings not in ["+", "*", "/", "%"]:
        print("Invalid input. Please enter one of the options.")
        continue
    if which_of_these_is_symbol_is_used_to_join_two_strings == "+":
        print("Correct! + is used to join two strings.")
        break
    else:
        print("Incorrect!.")
        try_again = input(
            "Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        print("Goodbye!")
    exit()
while True:
    which_of_these_is_a_comparison_operator = input(
        "Which of these is a comparison operator? +, not, and, ==: ")
    if which_of_these_is_a_comparison_operator not in ["+", "not", "and", "=="]:
        print("Invalid input. Please enter one of the options.")
        continue
    if which_of_these_is_a_comparison_operator == "==":
        print("Correct! == is a comparison operator.")
        break
    else:
        print("Incorrect!.")
        try_again = input(
            "Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        print("Goodbye!")
    exit()
print("Congratulations! You have completed the quiz.")

# STEPS AND EXPLANATION

'''
In this code i used three while loops because i provided 3 questions for the user

I gave each question a while loop so that when one question is answered it breaks and moves to the next
question. I also made it possible for the user to start again even when they chose the wrong answer.

Each while loop has a varaible where i assigned the ability for the user to select between
the provided options.

I considered the possibilty of a user inputing an answer totally different from the provided
options,to fix that the user will get notified to enter an answer from the options provided.

I gave each question a while loop so that when one question is answered it breaks and moves to the next
question. I also made it possible for the user to start again even when they chose the wrong answer.
'''
