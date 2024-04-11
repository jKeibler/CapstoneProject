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
ORANGE = (0,0.7,1)


led = RGBLED(red=17, green=18, blue=27)

while True:
    led.color = (0.2,0.7,0)
