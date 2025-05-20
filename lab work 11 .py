'''
Write a program to find the multiples of n, your loop should iterate 10 times.
'''
n = int(input("Enter a number: "))
for i in range(1, 10):
    n_multiples = n*i
    print(n_multiples)
