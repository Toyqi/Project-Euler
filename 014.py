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
