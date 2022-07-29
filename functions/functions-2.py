# f(x,3) = x**2 + 2*x*3 + 1


# function with default arguments
def f(x, y=3):
    print(x, y)
    return x ** 2 + 2 * x * y + 1


result1 = f(2)
result2 = f(2, 5)
result3 = f(y=10, x=12)  # calling function with keywords not by position


# function with multiple parameters
def f2(x, y, z):
    return x + y + z


print(f2(1, 2, 3))
test = (1, 2, 3)
print(f2(*test))  # tuple unpacking

print(f2(x=1, y=2, z=3))
test2 = {"x": 1, "y": 2, "z": 3}
print(f2(**test2))  # dictionary unpacking



