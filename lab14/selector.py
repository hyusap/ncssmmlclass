def main():
    # program selector
    print("1. Guessing Game")
    print("2. Number to Binary")
    print("3. Letter to ASCII")
    print("4. Score Average")
    choice = int(input("Enter a number: "))
    if choice == 1:
        import p1
    elif choice == 2:
        import p3
    elif choice == 3:
        import p4
    elif choice == 4:
        import p2
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
