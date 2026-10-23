def double_number(number):
    return number * 2


result = double_number(8)
print(result)

answer = double_number(6)
print(answer + 4)

answer = double_number(4)
print(answer + 5)

print(double_number(5))
print(double_number(3))
print(double_number(2.5))


def add_numbers(a, b):
    return a + b


print(add_numbers(6, 2))
print()

 
def subtract_numbers(a, b):
    return a - b

print(subtract_numbers(10, 4))
 

def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(3, 4))



def divide_numbers(a, b):
    return a / b

print(divide_numbers(10, 2))




def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))
print(safe_divide(10, 0))




def divide_input():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        print(safe_divide(a, b))
    except ValueError:
        print("Invalid number")


divide_input()
