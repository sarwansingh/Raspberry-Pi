import time
import RPi.GPIO as GPIO
# Pins definitions
btn_pin = 24
led_pin = 14
#supress warnings
GPIO.setwarnings(False)
# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
 
# If button is pushed, light up LED
try:
    while True:
        if GPIO.input(btn_pin):
            GPIO.output(led_pin, GPIO.HIGH)
        #time.sleep(1)
        else:
            GPIO.output(led_pin, GPIO.LOW)
        #time.sleep(1)

# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()
