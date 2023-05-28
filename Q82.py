# Q82. Write a Python program to interchange the first and last element in a list.

def interchange_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = input("Enter a list of elements: ").split()
result = interchange_first_last(my_list)
print("List after interchanging first and last element:", result)
