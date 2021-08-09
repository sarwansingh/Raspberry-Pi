import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)
####  Ultrasonic
TRIG = 5
ECHO = 6
####  LCD 
lcdrs=13
lcden=19
lcdd4=26
lcdd5=16
lcdd6=20
lcdd7=21

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

lcd = LCD.Adafruit_CharLCD(lcdrs, lcden, lcdd4,lcdd5 , lcdd6 , lcdd7 ,0 ,16,2)
lcd.message("    Welcome   ")
lcd.set_cursor(0, 1) #(col, row)
lcd.message("Height Mes. System")

while True :
    GPIO.output(TRIG, False)
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
    
    lcd.clear()
    lcd.message("Height =" )
    dis = '{0:0.1f}' .format(distance)
    lcd.message(dis)
    lcd.message(" cms")
    
    time.sleep(2)

