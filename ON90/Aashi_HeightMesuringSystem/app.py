from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
####  Ultrasonic
TRIG = 5
ECHO = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
##########
app = Flask(__name__)

@app.route("/")
def main():
    ###### getting value from ultrasonic
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
    dis = '{0:0.1f} cm' .format(distance)
    ########################
    
    templateData = {
       'height' :  dis
    }
    
    return render_template('index.html' , **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
