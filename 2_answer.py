
'''

    Project Euler Problem number 2
    limit for n is 4000000 ( 4 million )
    starting a and b will 1 , 2 respectively
    sum = even valued term of sequence
'''

sum = 2
a = 1
b = 2
c = 0
while True:
    c = a + b
    a = b
    b = c
    if c > 4000000:
        break
    else:
        if (c % 2) == 0:
            sum = sum + c
        else:
            continue
print (sum)