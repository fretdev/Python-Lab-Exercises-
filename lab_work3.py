bag_name = "Gucci"
sum_num = 2 + 2
michael_cgpa = 5.0
is_boy = True
print(str(michael_cgpa) + bag_name)
try:
    first_num = float(input("Enter First Number:"))
    second_num = float(input("Enter Second Number:"))
    operator = input("Enter Operator:")
    if operator == "+":
        sum_num = first_num + second_num
    elif operator == "-":
        sum_num = first_num - second_num
    elif operator == "*":
        sum_num = first_num * second_num
    elif operator == "/":
        if second_num == 0:
            print("Error: Division by zero is not allowed.")
            sum_num = None
        else:
            sum_num = first_num / second_num
    elif operator == "%":
        if second_num == 0:
            print("Error: Division by zero is not allowed.")
            sum_num = None
        else:
            sum_num = first_num % second_num
    print(sum_num)
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
