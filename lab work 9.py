'''
Write a program to keep asking for a number until you enter a negative number. At the end, 
print the sum of all entered numbers.
'''
numbers = []


while True:
    number = int(input("Enter number: "))
    numbers.append(number)
    if number < 0:
        break

print(sum(numbers))
