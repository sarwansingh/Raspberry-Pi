import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep

GPIO.setwarnings(False)     # disable the warning sign 
GPIO.setmode(GPIO.BCM)      # select the board type BCM 
GPIO.setup(15,GPIO.OUT)     # set the pin mode 

for i in range (5):
    GPIO.output(15, GPIO.HIGH)
    sleep(1)                 # takes seconds as argument 
    GPIO.output(15, GPIO.LOW)
    sleep(1)
    print(i)
