'''Q2. Why *args and **kwargs is used in some functions? 
Create a function each for *args and **kwargs
to demonstrate their use.'''

#  *args: accepts any number of arguments & returns the same
# **kwargs: accepts dictionary arguments

# *args
def test(*args):
    return args
print(test(1,13,"Ayan",[4,5,6,7],56.7,"Hello"))

# **kwargs
def test1(**kwargs):
    return kwargs
b=test1(Ayan= "My name", Age= 19, Gender= "Male")
for key, values in b.items():
    print(key," = ",values)
