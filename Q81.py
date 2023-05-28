# Q81. Write a Python program to find the n-th Fibonacci Number.

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n+1):
            a, b = b, a + b
        return b

number = int(input("Enter the value of n: "))
result = fibonacci(number)
print("The", number, "th Fibonacci number is:", result)
