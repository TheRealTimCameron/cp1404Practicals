"""
A.3
B.2
C.1
D.2
E.1 & 5
F.4
G.0
H.3
I. [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = "ten"
numbers[-1] = 1
past_2 = numbers[2:]
nine = 9 in numbers
print(past_2)
print(nine)
print(numbers)