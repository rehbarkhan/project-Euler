'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
flag = True 
number = 0
counter = 2520
while flag:
    for x in range(1,21):
        if (counter % x) != 0:
            break
        elif x == 20:
            print("Inside the Else statement")
            number = counter
            flag = False #While loop should end now
            break
        else:
            continue
    #print(counter)
    counter += 1

print(number)