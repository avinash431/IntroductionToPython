numbers = []
while True:
    number = int(input("Enter a number: "))
    numbers.append(number)
    msg = input("Do you want to add another number (y/n): ")
    if msg == "n":
        break

print(f"max number you've entered is {max(numbers)}")
print(f"min number you've entered is {min(numbers)}")
