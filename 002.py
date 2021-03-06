## Euler Problem 2

'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

## My Solution
'''
prev, cur = 0, 1
total = 0
maxNum = 4000000

while True:
    #temp = prev
    prev, cur = cur, prev + cur
    if cur >= maxNum:
        break
    if cur % 2 == 0:
        total += cur
print total
'''

## Official Solution
'''
Here is the beginning of the Fibonacci sequence with even numbers in red:
1 1 2 3 5 8 13 21 34 55 89 144 ...
a b c a b c a b c a b c
It is easy to prove that every third Fibonacci number is even.
'''
limit = 4000000
total = 0
a = 1
b = 1
c = a + b
while c < limit:
    total += c
    a = b + c
    b = c + a
    c = a + b

print total








    

