from gpiozero import Buzzer, RGBLED, DistanceSensor
from time import sleep
import math
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib
from LCD_Display.PCF8574 import PCF8574_GPIO
from LCD_Display.Adafruit_LCD1602 import Adafruit_CharLCD
from flask import Flask, render_template
from markupsafe import escape
import threading 


#For the GUI, web browser
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')


#To run this at 127.0.0.1:5000 
#flask --app app.py run
#To run in a better mode for reloads try this
#flask --app app.py run --debugger --reload --host=0.0.0.0

#BEFORE RUNNING ON PROJ RUN COMMAND
# cd myProj
#  . .venv/bin/activate
# 


current_time = datetime.now()

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
ORANGE = (0,0.7,1)

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
    num = unit * 100 /2.54 / 12
    return round(num,2)

#Creating a method to beep the sensor
def alert_beep():
    buzzer.on()
    sleep(0.25)
    buzzer.off()
    sleep(0.25)

#List of the email recipients,
email_recipients = ['keibler.joshua@gmail.com', 'rliddick@southhills.edu','cotto06@southhills.edu']

def send_emails():
    email_sender = 'jkeibler913@gmail.com'
    email_password = 'cbav ssng tlvl sqpy'
    subject = 'Security Alert! Trap Triggered!'
    body = f"""
        Hello Valued Customer,

    This is TripSys, your favorite home/business security system! We are contacting you to inform you of some activity.

    Our system has picked up some activity that had triggered the alarm. This happened on {current_time.strftime('%d/%m/%Y')}, at {current_time.strftime('%H:%M:%S')}.

    While we are not able to verify who or what triggered it, we encourage you to look into it, investigate, or possibly report to the police if it was clayton!

    Disclaimer: This is an automated email message. 

    Your local security system,
    - TripSys
    """
    #Defining the contents of the email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_recipients
    em['Subject'] = subject
    em.set_content(body)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender, email_password)
        for reciever in email_recipients:
            # Trying to change the persons name it is sent to
            # em['To'] = reciever
            smtp.sendmail(email_sender, reciever, em.as_string())
    pass

#---------------------------------------Execution---------------------------------------
led.color = ORANGE
calibrate_distance()
end = True

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)

lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

mcp.output(3,1)     # turn on LCD backlight
lcd.begin(16,2)



#Begin the loop for detection
while end == True:
    now = datetime.now()
    trapActive = True
    
    #Need multiple threads
    #app.run(host='0.0.0.0')
    
    
    if (trapActive == True):
        
        if ultrasonic_sensor.distance >= dist_to_wall - buffer_distance and ultrasonic_sensor.distance <= dist_to_wall + buffer_distance:
            led.color = GREEN
            
            lcd.clear()
            
            lcd.message('All Clear...\nAll Clear...')
        else:
            led.color = RED
            print(f"Alarm was Tripped at: {now}")
            alert_beep()
            
            lcd.clear()
            lcd.message("Intruder, Alert!\nIntruder, Alert!")
            
            #send_emails()
            #end = False
        sleep(0.05)
    
    

lcd.clear()
