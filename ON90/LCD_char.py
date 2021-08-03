import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcdrs=13
lcden=19
lcdd4=26
lcdd5=16
lcdd6=20
lcdd7=21

lcd = LCD.Adafruit_CharLCD(lcdrs, lcden, lcdd4,lcdd5 , lcdd6 , lcdd7 ,0 ,16,2)
lcd.message("IoT Champs")
lcd.set_cursor(0, 1) #(col, row)
lcd.message("Welcome")
 

