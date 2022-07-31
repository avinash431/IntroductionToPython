def function_return_multiple_values(x, y):
    sum_ = x + y
    sub_ = x - y
    mul_ = x * y
    return sum_, sub_, mul_


# a, b, c = function_return_multiple_values(2, 3)
# print(f"a is {a} b is {b} c is {c}")
#
#
# def search_number(search_num):
#     seq_numbers = [[100, 101], [102, 104, 105]]
#     found = False
#     for element in seq_numbers:
#         if search_num in element:
#             found = True
#             break
#     if found:
#         print(f"search number {search_num} is found")
#     else:
#         print(f"search num {search_num} is not found")
#
#
# def search_number_with_else(search_num):
#     seq_numbers = [[100, 101], [102, 104, 105]]
#     for element in seq_numbers:
#         if search_num in element:
#             print(f"search number {search_num} is found")
#             break
#     else:
#         print(f"search num {search_num} is not found")
#
#
# search_number_with_else(103)
#
#


def function_caller(func):
    func()


# function_caller(print_hello_world)


# def outer_function():
#     def inner_function():
#         print("This is a inner function")
#     print("This is a outer function")
#     return inner_function
#
#
# x = outer_function()
# x()


def f1(func):
    def wrapper():
        print("Calling the function")
        func()
        print("Function is executed")
    return wrapper


import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"time taken is {end - start}")
        return res
    return wrapper


@timer
def print_hello_world():
    print("hello world")


@timer
@f1
def print_avinash():
    print("Avinash")


@timer
def cal_sum(x, y):
    return x + y


print_avinash()
print(cal_sum(2, 3))
