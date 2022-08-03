def cal_divisor(x, y):
    print(f"x%y is {x % y}")
    print("last line of this function ran successfully")


def main():
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))

        cal_divisor(x, y)
    except Exception as e:
        print(str(e))
    print("Program is ended")


if __name__ == "__main__":
    main()
