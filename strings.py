#There are plenty of methods for strings
course = 'Python for Beginners'

#Printing the course variable in all uppercase, does not change variable
print(course.upper())
#Printing lowercase
print(course.lower())
#Searching to find if a string contains a letter or characters, returns the first instance
print(course.find('for'))
#replacing items in a string by passing in another string
print(course.replace('for', '4'))
#printing if there is the value in the variable as True/False
print('Python' in course)