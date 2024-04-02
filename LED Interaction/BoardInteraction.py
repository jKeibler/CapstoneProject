#Code for hardware interaction
#This just turns a green LED on and off
from gpiozero import LED
from time import sleep

led = LED(17)

#Turning the LED off
led.off()

#Keeping a counter so it will eventually stop
condition = True
counter = 0

#Keeping it in a loop so it will turn off and on
while condition == True:
    
    led.on()
    #sleeping for half a second so you can see it turn off and on
    sleep(0.3)
    led.off()
    #sleeping for half a second so you can see it turn off and on
    sleep(0.3)
    
    #Adding one to the counter so it will trip the condition 
    counter += 1
    #Printing the counters value
    print(int(counter))
    
    #Ending the program/stopping the flashing LED after a certain amount of time
    if counter >= 100:
        print(f"The LED has flashed {counter} times, program complete.")
        condition = False
        led.off()