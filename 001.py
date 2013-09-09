## Euler Problem 1

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
## My Solution
maxNum = 1000
result = 0

for i in range(maxNum):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print result
'''

## Official solution
target = 999
## If we had asked to do the same for all numbers less than 1,000,000,000

def SumDivisibleBy(n):
    p = target / n
    return n*(p*(p+1))/2

print SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)
