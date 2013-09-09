digits = []
digits.append('one'  )
digits.append('two'  )
digits.append('three')
digits.append('four' )
digits.append('five' )
digits.append('six'  )
digits.append('seven')
digits.append('eight')
digits.append('nine' )

tens = []
tens.append('twenty' )
tens.append('thirty' )
tens.append('forty'  )
tens.append('fifty'  )
tens.append('sixty'  )
tens.append('seventy')
tens.append('eighty' )
tens.append('ninety' )

hundred  = 'hundredand'
hundred2 = 'hundred'
thousand = 'onethousand'

teens = []
teens.append('ten'      )
teens.append('eleven'   )
teens.append('twelve'   )
teens.append('thirteen' )
teens.append('fourteen' )
teens.append('fifteen'  )
teens.append('sixteen'  )
teens.append('seventeen')
teens.append('eighteen' )
teens.append('nineteen' )

n = 0
for d in digits:
    n += len(d)
for t in teens:
    n += len(t)
for t in tens:
    n += len(t)
    for d in digits:
        n += len(t)
        n += len(d)
for h in digits:
    n += len(h)
    n += len(hundred2)
    for d in digits:
        n += len(h)
        n += len(hundred)
        n += len(d)
    for t in teens:
        n += len(h)
        n += len(hundred)
        n += len(t)
    for t in tens:
        n += len(h)
        n += len(hundred)
        n += len(t)
        for d in digits:
            n += len(h)
            n += len(hundred)
            n += len(t)
            n += len(d)
n += len(thousand)
print n
