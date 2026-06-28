try:
    num = int(input("Enter number: "))
    result = 10 / num

    print(result)

except ValueError:
    print("❌ Please enter numbers only")

except ZeroDivisionError:
    print("❌ Division by zero not allowed")