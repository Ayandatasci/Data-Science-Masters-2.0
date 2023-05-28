'''Q3. What is an iterator in python? 
Name the method used to initialise the iterator object and
the method used for iteration. Use these methods to print the 
first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].'''

# Iterator allows for efficient access to elements sequentially one at a time by next() method
# Method used to initialise the iterator object: iter()
# Method used for iteration: next()

list= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
list1= iter(list)
for i in range(5):
    print(next(list1))