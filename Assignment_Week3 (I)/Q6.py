'''Q6. Write a python program to print the first 
        10 Fibonacci numbers using a while loop.'''

n=int(input("Enter the range: "))
a=0
b=1
while n > 0 :
    print(a)
    a,b=b,a+b
    n=n-1