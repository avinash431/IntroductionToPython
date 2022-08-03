def cal_divisor(x, y):
    print(f"x%y is {x % y}")


def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    cal_divisor(x, y)

    print("Program is ended")


if __name__ == "__main__":
    main()
