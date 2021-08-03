import Adafruit_DHT
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

lcdrs=13
lcden=19
lcdd4=26
lcdd5=16
lcdd6=20
lcdd7=21 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4    #change pin no accordingly
lcd = LCD.Adafruit_CharLCD(lcdrs, lcden, lcdd4,lcdd5 , lcdd6 , lcdd7 ,0 ,16,2)
lcd.message("Weather Station")
lcd.set_cursor(0, 1) #(col, row)
lcd.message("from IoT champs")
time.sleep(10)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        lcd.clear()
        lcd.message("Temp ={0:0.1f}C ".format(temperature))
        lcd.set_cursor(0, 1)
        lcd.message("Humidity={0:0.1f}%".format( humidity))
    else:
        pass #print("Sensor failure. Check wiring.");
    time.sleep(1);

