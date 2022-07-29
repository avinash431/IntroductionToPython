"""
A sample program use-case of if else statement
"""

num1 = int(input("Enter a number: "))

"""
if else in traditional way
"""
if num1 % 2 == 0:
    odd_even = "even"
else:
    odd_even = "odd"

odd_even = "even" if num1 % 2 == 0 else "odd"  # if else with explicit boolean condition
odd_even = "odd" if num1 % 2 else "even"  # if else with Truthfulness
print(f"odd_even value is {odd_even}")


# Programming exercises
"""
1. Find the min of 3 numbers
2. Check whether year is leap year
3. Check whether string is palindrome
4. list empty -> empty or len
5. Check whether list has duplicates remove those duplicates
6. Find the middle num of the 3 numbers
"""
