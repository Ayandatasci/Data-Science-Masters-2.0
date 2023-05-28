'''Q4. Write a python program using reduce function to compute the product of a list containing numbers
from 1 to 25.'''
from functools import reduce
l1 = list(range(1, 26))
print(reduce(lambda x,y : x*y, l1))