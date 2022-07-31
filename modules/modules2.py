import modules

print(__name__)


def main():
    print(modules.cal_sum(2, 3))
    print(modules.cal_mul(4, 5))


if __name__ == "__main__":
    print("python is calling")
else:
    print("another module is calling")
