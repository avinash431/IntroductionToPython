# user input -> x
# x reverse
# x == x reverse => palindrome or not palindrome

x = input("Enter a string: ")
if x == x[::-1]:
    print("palindrome")
else:
    print("not palindrome")
    