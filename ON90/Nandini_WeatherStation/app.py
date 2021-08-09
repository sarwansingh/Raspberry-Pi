from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import Adafruit_CharLCD as LCD

app = Flask(__name__)
 
GPIO.setmode(GPIO.BCM)
led1 = 14 
led2 = 15
DHT11_pin = 4
lcdrs=13
lcden=19
lcdd4=26
lcdd5=16
lcdd6=20
lcdd7=21 
 
# Set each pin as an output and make it low:
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

lcd = LCD.Adafruit_CharLCD(lcdrs, lcden, lcdd4,lcdd5 , lcdd6 , lcdd7 ,0 ,16,2)
lcd.message("Weather Station")
lcd.set_cursor(0, 1) #(col, row)
lcd.message("from IoT champs")

 
@app.route("/")
 
def main():
   return render_template('index.html')
 
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<pin>/<action>")
def action(pin, action):
   temperature = ''
   humidity = ''
   if pin == "pin1" and action == "on":
      GPIO.output(led1, GPIO.HIGH)
    
   if pin == "pin1" and action == "off":
      GPIO.output(led1, GPIO.LOW)
    
   if pin == "pin2" and action == "on":
      GPIO.output(led2, GPIO.HIGH)
    
   if pin == "pin2" and action == "off":
      GPIO.output(led2, GPIO.LOW)
 
   if pin == "dhtpin" and action == "get":
      humi, temp = dht.read_retry(dht.DHT11, DHT11_pin)  # Reading humidity and temperature
      humi = '{0:0.1f}' .format(humi)
      temp = '{0:0.1f}' .format(temp)
      temperature = 'Temperature: ' + temp 
      humidity =  'Humidity: ' + humi
      
      lcd.clear()
      lcd.message("Temperature:" )
      lcd.message(temp)
      lcd.set_cursor(0, 1)
      lcd.message("Humidity:")
      lcd.message( humi)
 
   templateData = {
   'temperature' : temperature,
   'humidity' : humidity
   }
 
   return render_template('index.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
