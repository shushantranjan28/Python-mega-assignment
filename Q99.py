# Q99. Write a Python program to print the below pattern.

n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
