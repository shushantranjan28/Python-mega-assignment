# Q91. Write a Python program to merge two dictionaries.

def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
result = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", result)
