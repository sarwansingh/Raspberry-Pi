import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 6
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

time.sleep(2)
while True:
    print("Distance Check")
    
    GPIO.output(TRIG, False)
    print("Calming Down") # clear the pin and set high, wait for 10microsec and clear
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # wait 10 microsec.
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
   
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("distance:", distance, "cm")
  
    time.sleep(2)

