def main():
    x = int(input("Enter a positive number: "))
    if x < 0:
        raise ValueError("Enter positive number only")


if __name__ == "__main__":
    main()
