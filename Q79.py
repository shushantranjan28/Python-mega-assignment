# Q79. Write a Python program to check if a number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
