# Q92. Write a Python program to convert a list of tuples into a dictionary.

def convert_to_dictionary(lst):
    dictionary = dict(lst)
    return dictionary

my_list = [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
result = convert_to_dictionary(my_list)
print("Converted dictionary:", result)
