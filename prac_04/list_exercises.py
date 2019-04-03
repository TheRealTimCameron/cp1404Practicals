# No.1 Numbers stuff
numbers = []
for number in range(5):
    given_number = int(input("Number: "))
    numbers.append(given_number)
print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

# No.2 Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
given_username = input("Username: ")
while given_username != usernames:
    if given_username in usernames:
        print("Access granted")
        break
    else:
        print("Access denied")
        given_username = input("Username: ")