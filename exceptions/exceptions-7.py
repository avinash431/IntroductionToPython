def main():
    x = input("Enter a number: ")
    try:
        x = int(x)
        try:
            if x < 0:
                raise ValueError(f"Entered variable is -ve {x}")
        except ValueError as e:
            print(str(e))
    except ValueError as e:
        print(f"Entered variable is string {x}")


if __name__ == "__main__":
    main()