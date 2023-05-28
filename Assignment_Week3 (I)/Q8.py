'''Q8. Write a python program to check whether a given 
number is Palindrome or not using a while loop.'''

def palindrome(n):
    string_n=str(n)
    if string_n == string_n[::-1]:
        return True
    
n1=int(input("Enter the number to be checked: "))
if palindrome(n1):
    print("Its palindrome")
else:
    print("Its not palindrome")