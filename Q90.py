# Q90. Write a Python program to extract unique dictionary values.

def get_unique_values(dictionary):
    unique_values = list(set(dictionary.values()))
    return unique_values

my_dict = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1}
result = get_unique_values(my_dict)
print("Unique values in the dictionary:", result)
