try:
    number = int(input("Enter a number: "))
    print(number * 2)
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Program finished.")