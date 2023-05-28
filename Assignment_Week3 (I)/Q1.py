'''Q1. Which keyword is used to create a function?
Create a function to return a list of odd numbers
 in the range of 1 to 25.'''

#The keyword used to create a function in Python is def
def get_odd():
    odd_no = []
    for i in range(1, 25):
        if i % 2 != 0:
            odd_no.append(i)
    return odd_no

print(get_odd())