def calculator():
    while True:
        try:
            num1 = input("Enter the first number: ")
            if num1.lower() == "exit":
                print("Goodbye!")
                break

            num1 = float(num1)

            num2 = input("Enter the second number: ")
            if num2.lower() == "exit":
                print("Goodbye!")
                break

            num2 = float(num2)

            operation = input("Choose an operation (+, -, *, /): ")
            if operation.lower() == "exit":
                print("Goodbye!")
                break

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Calculation complete.")
