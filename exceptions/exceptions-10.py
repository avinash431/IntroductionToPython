def main():
    numbers_lst = []
    i = 0
    while i < 5:
        try:
            x = int(input("Enter a  positive number: "))
            if x < 0:
                raise ValueError("")
            numbers_lst.append(x)
            i += 1
        except ValueError:
            continue
    print(f"sum of numbers entered is {sum(numbers_lst)}")


if __name__ == "__main__":
    main()
