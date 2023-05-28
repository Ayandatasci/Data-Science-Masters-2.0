'''Q4. What is a generator function in python? 
Why yield keyword is used? Give an example of a generator function.'''

#generator function generates a sequence of values on-the-fly instead of returning them all at once
#yield keyword is used to pause the function's execution and yield a value to the caller

def neg_generator():
    n=0
    while True:
        yield n
        n=n+2
generator=neg_generator()
for i in range(5):
    print(next(generator))