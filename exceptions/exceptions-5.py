def main():
    try:
        x = int(input("Enter a number: "))
        y = int(input("Enter another number: "))
        try:
            print(f"x%y is {x%y}")
        except TypeError as e:
            print(str(e))
    except ValueError:
        print("Enter a number only")
    except Exception:
        print("Board Exception is being handled")


if __name__ == "__main__":
    main()