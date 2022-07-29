"""
A sample program with no condition in the while section
"""
nums_list = []
while True:
    num1 = int(input("Enter a  number: "))
    nums_list.append(num1)
    condition = input("Do you want to add another number(y/n): ")
    if condition == "n":
        break

print(f"{max(nums_list)} is the maximum number you've entered and {min(nums_list)} is the minimum number you have entered")