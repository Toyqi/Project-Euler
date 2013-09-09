## Euler Problem 6

'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

## My solution
## Such an approach would definitely get in trouble when limit becomes very large.
'''
sum1 = sum2 = 0
limit = 100

for i in range(1,limit + 1):
    sum1 += i * i
    sum2 += i

print sum2 * sum2 - sum1
'''

## Official Solution
'''
we are looking for a function f(n), that for any n gives the sum of 1^2 up to n^2. Assume it is of
the form f(n) = an^3 + bn^2 + cn + d, with a; b; c; d constants that we have to determine. This we can do
because we can verify that f(0) = 0; f(1) = 1; f(2) = 5; f(3) = 14.
Solving this system of equations, we obtain f(n) = 1/6(2n^3 + 3n^2 +n) = n(2n + 1)(n + 1)/6.
'''
limit = 100
sum1 = limit*(limit+1)/2
sum2 = (2*limit+1)*(limit+1)*limit/6
print sum1 * sum1 - sum2
