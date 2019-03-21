"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a character is entered that is not a number
2. When will a ZeroDivisionError occur?
When the denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes, see below
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Not valid!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

