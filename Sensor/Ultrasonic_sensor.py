from gpiozero import DistanceSensor
from time import sleep

trigPin = 23
echoPin = 24
sensor = DistanceSensor(echo=echoPin, trigger=trigPin, max_distance=13)

def loop():
    while True:
        print('Distance: ', sensor.distance * 100,'cm')
        sleep(1)

def convertInch():
    #Converting the distance to inches
    new_dist = sensor.distance * 100
    new_dist /= 2.54
    return new_dist

def convertFeet():
    new_dist = sensor.distance * 100
    new_dist /= 2.54
    return new_dist /12

def new_loop():
    while True:
        print(f"Distance: {convertInch()} inches.")
        sleep(.5)

if __name__ == '__main__': 
    print('Program is starting...')
    try:
        new_loop()
    except KeyboardInterrupt:
        sensor.close()
        print("Ending program")
    