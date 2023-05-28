# Q80. Write a Python program to check Armstrong Number.

def is_armstrong_number(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if n == sum:
        return True
    else:
        return False

number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
