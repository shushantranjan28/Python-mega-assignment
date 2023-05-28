# Q84. Write a Python program to find N largest elements from a list.

def find_n_largest_elements(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[:n]

my_list = input("Enter a list of elements: ").split()
n = int(input("Enter the value of N: "))
result = find_n_largest_elements(my_list, n)
print(n, "largest elements from the list:", result)
