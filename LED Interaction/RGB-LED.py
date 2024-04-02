from gpiozero import RGBLED
from time import sleep

RED = (0,1,1)
BLUE = (1,1,0)
GREEN = (1,0,1)
MAGENTA = (.5,1,0)
ELECTRIC_BLUE = (1,.5,0)
PINK = (.1,.9,.5)
YELLOW = (0,0,1)
PURPLE = (0,1,0)

led = RGBLED(red=17, green=18, blue=27)

condition = True
counter = 0

while condition == True:
    
    #Sets the color to blue
    led.color = BLUE
    sleep(1)
    
    #Sets the color to red
    led.color = RED
    sleep(1)
    
    #Sets the color to green
    led.color = GREEN
    sleep(1)
    
    
    counter += 1
    print(int(counter))
    
    if counter >= 100:
        condition = False
        print(f"You have flashed {counter * 3} colors.")