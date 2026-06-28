try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Enter (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)

    elif operation == "-":
        print("Result:", num1 - num2)

    elif operation == "*":
        print("Result:", num1 * num2)

    elif operation == "/":
        print("Result:", num1 / num2)

    else:
        print("❌ Invalid Operation")

except ValueError:
    print("❌ Enter numbers only")

except ZeroDivisionError:
    print("❌ Cannot divide by zero")