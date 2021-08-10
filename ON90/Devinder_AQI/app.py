from flask import Flask, render_template, request

app = Flask(__name__)

AQI = 12.5

@app.route("/")
def abc():
    return render_template("index.html" , data=AQI) 
    #return " IoT Champs "

if __name__  == "__main__" :
    app.run()