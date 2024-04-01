#Range generates a range of numbers from 0 to the number passed into it
numbers = range(5)
#printing out the numbers in the range
#This format is specifically how you print items within a range
for number in numbers:
    print(number)

#This gives the range a start point (5) and end point (10)
problems = range(5,10)
for number in problems:
    print(number)

#This is using a step with the range function
#this tells the method how much to increase by
items = range(20,30, 2)
for number in items:
    print(number)