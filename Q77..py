# Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (PRT)/100.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)
