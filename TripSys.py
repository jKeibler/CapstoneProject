from gpiozero import Buzzer
from gpiozero import RGBLED
from gpiozero import DistanceSensor
from time import sleep
import math

#Setting up the RGB LED to the GPIO connections
led = RGBLED(red=17, green=18, blue=27)

#Setting up the Buzzer to a GPIO connections
buzzer = Buzzer(22)

#Setting up the Ultrasonic Sesnro to the GPIO connections
#First must setup the trigger pins and echo pins 
trigger_pin = 23
echo_pin = 24
ultrasonic_sensor = DistanceSensor(trigger=trigger_pin, echo=echo_pin, max_distance=13)

#Colors stored in variables for ease of access
RED = (0,1,1)
BLUE = (1,1,0)
GREEN = (1,0,1)
MAGENTA = (.5,1,0)
ELECTRIC_BLUE = (1,.5,0)
PINK = (.1,.9,.5)
YELLOW = (0,0,1)
PURPLE = (0,1,0)

#Defining a list of numbers for calibration, numbers in cm
calibration = []


#Defining a global for wall distance
dist_to_wall :float
#Defining a buffer distance for 
buffer_distance = 0.1


#Defining methods 

#Calibration Method for initializing
def calibrate_distance():
    global calibration, dist_to_wall
    print("Calibrating distance, please wait.")
    calibration.clear()
    counter = 0
    while counter <= 20:
        calibration.append(ultrasonic_sensor.distance)
        sleep(.1)
        counter += 1
    calibration.sort()
    calibration = calibration[2:18]
    
    dist_to_wall = sum(calibration)/len(calibration)
    print(f"{convert_to_feet(dist_to_wall)} feet to surface.")

    print("Calibration complete.")


#Writing a method to convert distance to feet
def convert_to_feet(unit):
    return unit * 100 /2.54 / 12

#Creating a method to beep the sensor
def alert_beep():
    #Creating a counter for now, later it should stop as soon as someone stops
    counter = 0
    while counter <= 5:
        buzzer.on()
        sleep(0.5)
        buzzer.off()
        sleep(0.5)
        counter += 1
    

#---------------------------------------Execution---------------------------------------
led.color = ELECTRIC_BLUE
calibrate_distance()
print(min(calibration))
print(max(calibration))

while ultrasonic_sensor.distance >= dist_to_wall - buffer_distance and ultrasonic_sensor.distance <= dist_to_wall + buffer_distance:
    led.color = GREEN
    print("In range")
    sleep(0.5)

led.color = RED
print("Out of range")
print("Program Terminated!")
sleep(2)