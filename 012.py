## Euler Problem 12
'''
What is the value of the first triangle number to have over five hundred divisors?
'''
def nFactors(x):
    nF = 0
    for i in range(2,x/2):
        nF = nF + (x%i==0)
    return nF

i = 0
while True:
    i += 1
    A = i
    B = i+1
    nFA = nFactors(A)
    nFB = nFactors(B)
    if nFA*nFB >= 500:
        print A*B/2
        break