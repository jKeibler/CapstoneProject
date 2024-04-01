#The input function returns a string, so this will automatically fail
# birth_year = input("Enter your birth year: ")
# age = 2020 - birth_year
# print(age)

#This converts the string from the input function to an integer
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
#You must convert variables to strings to print them or your program will crash
print("You are " + str(age) + " years old.")

#There are many types of conversions

#Conversion to a float, or decimal
float(age)
#Conversion to a int, or number
int(age)
#Conversion to a boolean, or True/Flase
bool(age)
#Conversion to a string, or characters
str(age)