# QUESTIONS
# Imagine the price of a house is 1million, Write a program that collects the user input
# of the house price they budgeted, Use the if statement to check if the user’s price is
# below 500000 and above 300000, then print the downpayment with 10%, otherwise if the user’s price
# is above 500000 and print the downpayment with 20%.The formula to calculate down-payment is (given
# percentage divided by 100 multiplied by price of house).

# SOLUTION

while True:
    try:
        house_price = 1000000
        house_budget = float(input("Enter your house budget: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    if house_budget < 500000 and house_budget > 300000:
        down_payment = (10/100) * house_price
        print(f"Your Down payment is {down_payment}")
    elif house_budget > 500000:
        down_payment = (20/100) * house_price
        print(f"Your Down_payment is {down_payment}")
    else:
        print("Your house budget is too low.")

        enter_a_new_house_budget = input(
            "Do you want to enter a  new house_budget? (yes/no):").strip().lower()
        if enter_a_new_house_budget != 'yes':
            print("Goodbye!")
            break


# MY STEPS AND EXPLANATION

'''
Using the while loop, i created the variable house_price to hold the price of the house

My next step was i gave the user the ability to enter their budget

To prevent the user from entering another data type order than a numeric value
i used try and except to alert the user anytime they input a value other than a float.

Then after that i went on to create my conditional statements where the user gets the liberty
to pay a downpayment of 10% or 20% given the amount they budgeted matches my conditions.

i used an else statement that alerts the user when their budget is too low

I also made it possible for the user to enter a new budget if they want to my code reruns if not they get
a GOODBYE!! message and my code or program ends.
'''
