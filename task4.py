#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""

import operator

question = ("enter a length in centimeters: ")

a = float(input(question))

F = a/30.48
F = round(F,0)

t = a% 30.48

i = round(t/2.54,0)

print(f"{a} centimeters is {F} feet and {i}inches.")






