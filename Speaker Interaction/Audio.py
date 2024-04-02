from gpiozero import Buzzer 
from time import sleep

bz = Buzzer(22)

condition = True
counter = 0

while condition == True:
    bz.on()
    sleep(1)
    bz.off()
    sleep(1)
    counter += 1
    
    if counter >= 20:
        condition = False
        print(f"All Done. {counter} many beeps made.")

