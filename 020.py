import math
n = math.factorial(100)
sum = 0
while n > 0:
    d = n%10
    sum += d
    n = (n-d)/10
print sum
