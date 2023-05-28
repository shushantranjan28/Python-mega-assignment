# Q76. Write a Python program to find the factorial of a given number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is", result)


