"""
This is a test module for python functions
which has docstrings, recursion, inner functions examples
"""


def f3():
    """
    This is a simple function for testing
    :return:
    """


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def cal_sum(a, b):
    return a + b


lambda_cal_sum = lambda a, b: a + b
print(lambda_cal_sum(2, 3))

x = [[1, 2], [4, 1], [3, 0]]
print(sorted(x, key=lambda y: y[1]))

y = {4: "java", 3: "python", 1: "c++", 2: "c"}
print(y.items())
print(sorted(y.items(), key=lambda z: len(z[1])))

z = ["python", "c++", "c", ".net", "java"]
print(sorted(z, key=len))


def fibonacci(n):
    start, end = 0, 1
    for _ in range(n-1):
        start, end = end, start + end
    return end


print(fibonacci(15))


def fibonacci_recursion(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


"""
f(x,y) = x**2 + 2 * x+y + 3
1. Input shouldn't be modified
2. Treat functions as first class objects
"""

