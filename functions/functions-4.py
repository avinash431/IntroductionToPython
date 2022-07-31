x = 15
z = [1, 2, 3, 4]


def f1():
    x = 5
    print(f"x in f1 fun is {x}")
    z.append(10)
    print(f"y in f1 fun is {z}")


def f2():
    x = 10
    global y
    y = 20
    f1()
    print(f"x in f2 fn is {x}")


def f3():
    print(x)


print(f"z before calling f2 is {z}")
f2()
print(f"x in main fn is {x}")
print(f"z after calling f2 is {z}")
y = 10
print(f"y in main fn is {y}")

