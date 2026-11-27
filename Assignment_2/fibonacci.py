def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


try:
    n = int(input("Enter number of terms: "))

    if n <= 0:
        print("Enter a positive number.")
    else:
        print("Fibonacci series:")
        fibonacci(n)
except ValueError:
    print("Enter a whole number.")
