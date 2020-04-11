'''

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

    x will hold the large value
    leftValue,rightValue
    product
    for x in range(100,1000)
    for y in range(100,1000)
        product = (x * y)
        if product is pallindrom
            leftVale = x , rightValue = y


'''

def pallindrom(x):
    if str(x) == (str(x)[::-1]):
        return True
    else:
        return False

def compare(number,x,y,leftVal,rightVal):
    if (x*y) >= number:
        leftVal = x 
        rightVal = y
        return(leftVal,rightVal,x*y)
    else:
        return(leftVal,rightVal,number)


leftValue = 0 
rightValue = 0
number = 0
for x in range(100,1000):
    for y in range(100,1000):
        if pallindrom(x*y):
            leftValue,rightValue,number=compare(number,x,y,leftValue,rightValue)
        else:
            continue

print(str(leftValue)+" "+str(rightValue)+" "+str(number))

