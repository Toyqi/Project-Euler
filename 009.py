## Euler Problem 9

'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
limit = 1000
flag = False
for a in range(1, limit -1):
    for b in range(a, limit - a):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            flag = True
            break
    if flag == True:
        break
    
print a*b*c

