# Q85. Write a Python program to find the cumulative sum of a list.

def cumulative_sum(lst):
    cum_sum = []
    current_sum = 0
    for num in lst:
        current_sum += num
        cum_sum.append(current_sum)
    return cum_sum

my_list = input("Enter a list of elements: ").split()
my_list = [int(x) for x in my_list]
result = cumulative_sum(my_list)
print("Cumulative sum of the list:", result)
