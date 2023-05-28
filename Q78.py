# Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

compound_interest = principal * ((1 + rate / 100) ** time)
print("The compound interest is:", compound_interest)
