try:
    number = float(input("Enter a number: "))
    print(number * 2)
except ValueError:
    print("Invalid number")