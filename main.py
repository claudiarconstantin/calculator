import calculator

# Calculator wirth preconfigured values
result_add = calculator.adding(10, 5)
print(f"Adding: {result_add}")

result_sub = calculator.subtracting(10, 5)
print(f"Subtracting: {result_sub}")


#Calculator with inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result_add = calculator.adding(num1, num2)
print(f"Adding: {result_add}")

result_sub = calculator.subtracting(num1, num2)
print(f"Subtracting: {result_sub}")