def cal_divisor(x, y):
    try:
        print(f"x%y is {x % y}")
    except ZeroDivisionError as e:
        print(str(e))
    print("last line of this function ran successfully")


def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))

    cal_divisor(x, y)

    print("Program is ended")


if __name__ == "__main__":
    main()
