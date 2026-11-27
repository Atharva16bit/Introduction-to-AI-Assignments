def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Enter numbers only.")
        continue

    if choice == "1":
        print("Answer:", add(a, b))
    elif choice == "2":
        print("Answer:", subtract(a, b))
    elif choice == "3":
        print("Answer:", multiply(a, b))
    else:
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print("Answer:", divide(a, b))
