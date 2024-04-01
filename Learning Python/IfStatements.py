temperature = 23

#Format for printing when the weather temperature is within a certain range
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: #from 20-30
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")