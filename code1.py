

def greet(name):
    print(f"Hello, {name}! Welcome to GitHub practical.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    greet("Student")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")
