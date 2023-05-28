'''Q5. Create a generator function for prime numbers less than 1000. 
Use the next() method to print the first 20 prime numbers.'''

def prime_generator():
    primes = []
    n = 2
    while True:
        count=0
        for i in range(1, n+1):
            if (n%i==0):
                count+=1
        if (count == 2):
            primes.append(n)
            yield n
        n=n+1

generator = prime_generator()
print("The first 20 prime numbers are:")
for i in range(20):
    print(next(generator))