# Q88. Write a Python program to check if a substring is present in a given string.

def is_substring_present(string, substring):
    if substring in string:
        return True
    else:
        return False

main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to search for: ")
if is_substring_present(main_string, sub_string):
    print(sub_string, "is present in the main string.")
else:
    print(sub_string, "is not present in the main string.")

