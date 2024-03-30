first = input("First Number: ")
second = input("Second Number: ")
#Instead of converting to int where decimals cannot be used, convert to float
sum = float(first) + float(second)
#Dont forget to convert to str when printing to avoid errors
print("Sum: " + str(sum))


#same as before, but you can convert eariler
first = float(input("First Number: "))
second = float(input("Second Number: "))
sum = first + second
print("Sum: " + str(sum))