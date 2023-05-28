# Q98. Write a Python program to print the below pattern.

n = 5
for i in range(1, n+1):
    for j in range(n, i-1, -1):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()
