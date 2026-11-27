def is_prime(n):
    if n < 2:
        return False

    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


try:
    n = int(input("Enter a number: "))

    if is_prime(n):
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
except ValueError:
    print("Enter a whole number.")
