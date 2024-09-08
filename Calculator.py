def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Get user input for operation
    operation = input("Enter the number of the operation (1/2/3/4): ")

    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform the calculation based on the chosen operation
    if operation == '1':
        result = add(num1, num2)
        op_symbol = '+'
    elif operation == '2':
        result = subtract(num1, num2)
        op_symbol = '-'
    elif operation == '3':
        result = multiply(num1, num2)
        op_symbol = '*'
    elif operation == '4':
        result = divide(num1, num2)
        op_symbol = '/'
    else:
        print("Invalid operation choice.")
        return

    # Display the result
    print(f"{num1} {op_symbol} {num2} = {result}")

if __name__ == "__main__":
    main()
