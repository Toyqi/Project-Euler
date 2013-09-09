## Euler Problem 4

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def isPalindrome(number):
    number = str(number)
    reverse = number[::-1]
    if number == reverse:
        return True
    else:
        return False
    
## My Solution
'''
actualProduct = 0
highestPalindrome = 0

num1 = 100
num2 = 999
 
#a = 0
#b = 0


for i in range(num1, num2+1):
    for j in range(i, num2+1):
        # Originally for j in range(num1, num2+1)
        # The number 69696 is checked both when i=132 and j=528 and when i=528 and j=132.
        # To stop checking numbers like this we can assume i ¡Ü j
        actualProduct = i * j
        if (isPalindrome(actualProduct)) and (highestPalindrome < actualProduct):
            highestPalindrome = actualProduct
            #a = i
            #b = j

#print "Largest palindrome made from the product of two %d-digit numbers is [ %d ] made of %d * %d" % (len(str(num1)), highestPalindrome, a, b)
print highestPalindrome
'''

## Official Solution 1
'''
largestPalindrome = 0
a = 999
  
while a >= 100:
    b = 999
    while b >= a:
        if a*b <= largestPalindrome:
            break    # Since a*b is always going to be too small
        if isPalindrome(a*b):
            largestPalindrome = a * b
        b -= 1
    a -= 1

print largestPalindrome
'''

## Official Solution 2
## A faster solution
largestPalindrome = 0
a = 999

while a >= 100:
    if a % 11 == 0:
        b = 999
        db = 1
    else:
        b = 990          # The largest number less than or equal 999
                         # and divisible by 11
        db = 11
    while b >= a:
        if a*b <= largestPalindrome:
            break    
        if isPalindrome(a*b):
            largestPalindrome = a * b
        b -= db
    a -= 1

print largestPalindrome
