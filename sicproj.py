def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print("Simple Calculator")
print("1. Add")
print("2. Subtract")

choice = input("Choose an option (1 or 2): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
else:
    print("Invalid choice!")
