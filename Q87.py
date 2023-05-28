# Q87. Write a Python program to remove the i'th element from a string.

def remove_ith_element(string, i):
    if i < 0 or i >= len(string):
        return string
    else:
        return string[:i] + string[i+1:]

word = input("Enter a word: ")
position = int(input("Enter the position of the element to remove: "))
result = remove_ith_element(word, position)
print("String after removing the", position, "element:", result)
