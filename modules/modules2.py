import modules as md

print(__name__)


def main():
    print(md.cal_sum(2, 3))
    print(md.cal_mul(4, 5))


if __name__ == "__main__":
    print("python is calling")
    main()
else:
    print("another module is calling")
