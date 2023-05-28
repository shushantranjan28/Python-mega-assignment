# Q94. Write a Python program to get all combinations of 2 tuples.

import itertools

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)

result = list(itertools.product(test_tuple1, test_tuple2))
print("All combinations of two tuples:", result)
