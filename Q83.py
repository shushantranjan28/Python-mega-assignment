# Q83. Write a Python program to swap two elements in a list.

def swap_elements(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst

my_list = input("Enter a list of elements: ").split()
position1 = int(input("Enter the position of the first element to swap: "))
position2 = int(input("Enter the position of the second element to swap: "))
result = swap_elements(my_list, position1, position2)
print("List after swapping elements:", result)
