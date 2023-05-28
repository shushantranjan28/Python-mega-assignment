# Q93. Write a Python program to create a list of tuples from a given list having a number and its cube in each tuple.

def create_tuple_list(lst):
    tuple_list = [(num, num**3) for num in lst]
    return tuple_list

my_list = [9, 5, 6]
result = create_tuple_list(my_list)
print("List of tuples:", result)
