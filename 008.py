## Euler problem 8
## Find the greatest product of five consecutive digits in the 1000-digit number.

infile = file('008_digit.txt', 'r')

# first read file into list
tempVar = []
for line in infile.readlines():
    tempVar.append(line)

# take all the lines, put them in one big string
y = ''.join(tempVar)

# get rid of the \n new line char
finish = y.replace('\n','')

# now you have a huge string
maxValue = 0
for i in range(1000-5):
    product = int(finish[i]) * int(finish[i+1]) * int(finish[i+2]) * int(finish[i+3]) * int(finish[i+4])
    if product >= maxValue:
        maxValue = product
print maxValue
