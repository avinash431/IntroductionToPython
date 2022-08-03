try:
    x = 1
    y = 2
    print(x % y)
except ZeroDivisionError as e:
    pass
else:
    print("try ran successfully")
