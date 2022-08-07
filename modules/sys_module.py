import sys


x = 10
print(sys.getsizeof(x))
print(x, file=sys.stdout)
print(sys.version)
print(sys.version_info)

try:
    y = 20/0
    print("After the exception is raised")
except Exception as e:
    print(str(e))
    sys.exit(10)

