## Euler Problem 3
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

## My Solution
import math
test = 3
num = 600851475143
s = math.sqrt(num)
lastestNum = 0
while num % 2 == 0:
    num /= 2
while num > 1 and test < s :
    if num % test == 0:
        num /= test
        lastestNum = num
        s = math.sqrt(num)
    else:
        test += 2
print lastestNum
