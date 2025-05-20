# QUESTION
# Given an integer n, perform the following conditional actions
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# SOLUTION
while True:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number")
        continue  # ask again if invalid input

    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 5):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 20):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

    try_again = input("Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        print("Goodbye!")
        break

        # MY STEPS AND EXPLANATION

    '''
     I used the % operator to check if the number is odd or even by checking if when divided
       by 2 it has a remainder

    I used the range function to check if the number is in range of 2 to 5 and 6 to 20

    i also used the in operator to check if the number is in the range

    i used the if and elif statements to check the conditions

    

                      EDGE CASES

    Using the While loop i used try and except to check if the input is a number

    If input is not an integer the user will be asked to enter a valid number

    It will continue to ask for a number until a valid number is entered

    After my conditionals i used the try again statement to ask the user if they want to try again

    If the user enters yes the program will continue

    If the user enters no the program will exit by warmly saying Goodbye!

I used the strip and lower methods to remove any spaces and convert the input to lowercase
 so incase we have a foolish user

who enters Yes or YES the program will still work

I also used the break statement to exit the loop if the user enters no

THANK YOU MR BESTZ FOR THIS ASSIGNMENT
'''
