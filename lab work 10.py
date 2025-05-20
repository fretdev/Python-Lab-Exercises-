'''
Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."
'''
names = []
while True:
    name = input("Enter a name: ")
    names.append(name)

    choice = input("Do you want to end this program(N / END): ")
    if choice.upper() == 'N':
        print(name)
    elif choice.upper() == 'END':
        print("I am done.")
        break

for x in names:
    print(x)
