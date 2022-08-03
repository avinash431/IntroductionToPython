def main():
    try:
        x = int(input("Enter a number: "))
        try:
            if x < 0:
                raise ValueError(f"Entered variable is -ve {x}")
        except ValueError as e:
            print(str(e))
    except ValueError as e:
        print(f"Entered variable is string {x}")
    finally:
        print("Printing in finally block")


if __name__ == "__main__":
    main()