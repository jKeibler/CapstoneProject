#This is the syntax to define a method
#The keyword def is used to start it, then you use (): after you name your method
def hello():
    print("Hello")
    print("It is nice to meet you!")

#This is how you use parameters
#This is also how you use string interolation in python
def name_hello(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

name_hello('Joshua', 'Keibler')
name_hello("John", "Smith")

#-----Returning values/items with methods -----
#All methods return none by default
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Josh")
print(message)

def increment(number,by):
    return number + by
#Using a hidden variable to print, still works fine
print(increment(3, 1))
#You can explicitly say your variable names
print(increment(3, by=1))

#This is an optional parameter, it is possible by giving a parameter a default value
#All required parameters must come first before default parameters
def incrementing(number, by=1):
    return number + by
print(incrementing(4))


#using a tuple list for a parameter
#make sure to return in the outest most layer or it will return everytime the loop executes
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2,3,4,5))

#Double asterisk means passing multiple key value pairs is possible
#Contains Key value pairs
#This is a dictionary (user)
def save_user(**user):
    print(user)
    #you can also print out specific values from keys
    print(user['name'])

save_user(id=1,name='John',age=22)
