import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import Adafruit_DHT
import datetime
import time
import Adafruit_CharLCD as LCD

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Relay1 =3 # pin3
Relay2=11

btn_pin=10

lcdrs=13
lcden=19
lcdd4=26
lcdd5=16
lcdd6=20
lcdd7=21 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4 

GPIO.setup(Relay1, GPIO.OUT)   
GPIO.setup(Relay2, GPIO.OUT)

ledRed = 10
ledYlw = 12

sensor = 16
buzzer = 18

#GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledYlw, GPIO.OUT)

lcd = LCD.Adafruit_CharLCD(lcdrs, lcden, lcdd4,lcdd5 , lcdd6 , lcdd7 ,0 ,16,2)
lcd.message("Home Automation")
lcd.set_cursor(0, 1) #(col, row)
lcd.message("from Ankita")
time.sleep(2)

@app.route("/")
def main():
    # Read Sensors Status
    ledRedSts = GPIO.input(ledRed)
    ledYlwSts = GPIO.input(ledYlw)
    
    templateData = {
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts 
              
          }
    return render_template('main.html', **templateData)
    
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
 
    #if deviceName == "dhtpin" and action == "get"   :
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    ledRedSts = GPIO.input(ledRed)
    ledYlwSts = GPIO.input(ledYlw)
    templateData = {
              'ledRed'  : ledRedSts,
              'ledYlw'  : ledYlwSts,
              'Temperature' : temperature,
              'Humidity' : humidity
          }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run()
