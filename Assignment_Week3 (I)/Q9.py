'''Q9. Write a code to print odd numbers from 1 to 100
         using list comprehension.'''

numbers = list(range(101))
odd_no = list(filter(lambda x : x%2 != 0, numbers))
print(odd_no)