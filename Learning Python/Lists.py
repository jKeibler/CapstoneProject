#Creating a list full of names
names = ["John", "Bob", "Mary", "Ethan", "Juan"] 
print(names)

#Retrieving items in a list by index
#An index starts at 0 instead of 1
print(names[0])

#this retrieves the last item in a index by specifying -1
print(names[-1])

#you can retrieve elements by saying -2 it will start from the end of the list
print(names[-2])

#you can change elements by specifying the element
names[0] = 'Jon'
print(names[0])

#this is how you print indexes in a range
print(names[0:3])