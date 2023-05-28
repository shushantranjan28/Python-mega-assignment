# Q95. Write a Python program to sort a list of tuples by the second item.

def sort_tuples_by_second_item(tuple_list):
    sorted_list = sorted(tuple_list, key=lambda x: x[1])
    return sorted_list

tuple_list = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
result = sort_tuples_by_second_item(tuple_list)
print("List of tuples sorted by the second item:", result)
