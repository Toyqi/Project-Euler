## Euler Problem 7
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
#! -*- encoding: utf-8 -*-
import math

def isPrime(n):
    # an even number cant be a prime (divisible by 2)
    # 1 and 0 are no primes
    # special case: 2 is a prime
    if (n % 2 == 0 and n != 2) or n <= 1:
        return False

    # get a list of all uneven numbers above 3 till the sqrt of n + 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


i = 0
primes = []
while len(primes) != 10001:
    if i < 3:
        i += 1
    else:
        i += 2
    if isPrime(i):
#        if i < 20:
#            print "{0} {1}".format(len(primes)+1, i)
        primes.append(i)

print primes[-1:]
