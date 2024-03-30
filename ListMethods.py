numbers = [1,2,3,4,5]
print(numbers)

#Appending a number to a list then printing it out again
numbers.append(6)
print(numbers)

#inserting, this method expects two parameters
#the first parameter is the index of the list and the next is the object(anything)
numbers.insert(0, -1)
print(numbers)

#This removes a value in the list
numbers.remove(5)
print(numbers)

#checking if 1 is in the numbers list, returns a boolean value
print(1 in numbers)

#determins the amount of things in a list
print(len(numbers))

#how to clear a list, doesnt expect parameters
numbers.clear()
print(numbers)
