def calculator():
    """
    A simple command-line calculator that performs basic arithmetic operations.
    """
    print("--- Welcome to the Cool Calculator! ---")
    print("Operations: +, -, *, /, % (modulo), ** (power)")
    print("Enter 'exit' at any time to quit.")
    print("-" * 35)

    while True:
        try:
            num1_str = input("Enter the first number (or 'exit'): ")
            if num1_str.lower() == 'exit':
                break
            num1 = float(num1_str)

            operator = input("Enter an operator (+, -, *, /, %, **): ")
            if operator.lower() == 'exit':
                break

            num2_str = input("Enter the second number (or 'exit'): ")
            if num2_str.lower() == 'exit':
                break
            num2 = float(num2_str)

            result = None
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
            elif operator == '%':
                if num2 == 0:
                    print("Error: Modulo by zero is not allowed!")
                    continue
                result = num1 % num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print("Error: Invalid operator. Please use +, -, *, /, %, or **.")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")
            print("-" * 35)

        except ValueError:
            print("Error: Invalid input. Please enter numbers for calculations.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("--- Thanks for using the Cool Calculator! Goodbye! ---")

# Run the calculator
if __name__ == "__main__":
    calculator()
