## Euler Problem 14

'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
results = []
def step(x, n, start):
    if x%2==0:
        if x/2<start:
            return n + results[x/2]
        else:
            return step(x/2, n+1, start)
    else:
        return step(3*x+1, n+1, start)

results.append(0)
results.append(0)
highest_result = 0
highest_seed   = 0
for i in range(2,1000000):
    answer = step(i,0,i)
    results.append(answer)
    if answer > highest_result:
        highest_result = answer
        highest_seed = i

print highest_seed
