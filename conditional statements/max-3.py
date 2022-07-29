"""
A program to find the maximum of 3 numbers passed by the user
using if else condition
"""

num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
num3 = int(input("Enter number3 "))

"""
One way of finding the maximum of three numbers
checking number to another one using nested if and else condition
"""
if num1 > num2:
    if num1 > num3:
        print("num1 is the largest")
    else:
        print("num3 is the largest")
else:
    if num2 > num3:
        print("num2 is the largest")
    else:
        print("num3 is the largest")

"""
Best way of finding the maximum of 3 numbers
using only if condition
"""
max_num = num1
if max_num < num2:
    max_num = num2
if max_num < num3:
    max_num = num3

print(f"{max_num} is the largest")
