#First we have to convert the string to a number to do math to it
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
#Next we have to decide which way they would like the weight converted
if unit.upper() == 'K':
    converted = weight / 0.45
    #Dont forget we have to convert type to string to print
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    #Dont forget we have to convert type to string to print
    print("Weight in Kgs: " + str(converted))