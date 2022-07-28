num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
num3 = int(input("Enter number3 "))

# if num1 > num2:
#     if num1 > num3:
#         print("num1 is the largest")
#     else:
#         print("num3 is the largest")
# else:
#     if num2 > num3:
#         print("num2 is the largest")
#     else:
#         print("num3 is the largest")

max_num = num1
if max_num < num2:
    max_num = num2
if max_num < num3:
    max_num = num3

print(f"{max_num} is the largest")
