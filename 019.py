days = [31,28,31,30,31,30,31,31,30,31,30,31]

n=0
d=2 # Jan 1st 1901 was a Tuesday
for y in range(1,101):
    for m in range(0,12):
        d += days[m]
        if m==1 and y%4==0:
            d += 1
        if d%7==0:
            n+=1
print n
