'''
Using the loop, write a program that prints the sum of numbers in a list of 10 numbers 

'''
# Method 1
'''
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
sum_of_numbers = 0
for x in numbers:
 sum_of_numbers += x
 print("The sum of the numbers in the list is:", sum_of_numbers)
'''

# Method 2

numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
total = 0
for x in range(0, len(numbers)):
    total = total + numbers[x]
print("The sum of the numbers in the list is:", total)
