def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    # Return all prime numbers less than or equal to n
    primes = []
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes

n=int(input('Podaj ostatnia liczbe przedzialu: '))
primes = sieve_of_eratosthenes(n)
print(primes) # prints [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
