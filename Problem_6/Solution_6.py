'''
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025−385=2640.
Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
'''

square_of_each_number = 0
total_square_number = 0
difference_value = 0
for x in range(1,101):
    total_square_number = total_square_number + x
    square_of_each_number = square_of_each_number + (x * x)
print(total_square_number*total_square_number)
print(square_of_each_number)
difference_value = (total_square_number * total_square_number) - square_of_each_number
print(difference_value)