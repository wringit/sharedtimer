from flask import Flask, redirect, url_for, render_template, request # Flask class which will be instantiated
import timer
import codes
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/timerCodes/<code>', methods=['POST','GET'])
def getTime(code):
    if request.method == "POST":
        if request.form["action"] == "PAUSE":
            timer.timers[code][1] = not timer.timers[code][1]
    else:
        try:
            return timer.timers[code][0]
        except:
            return "error"


@app.route('/create', methods=['POST'])
def create():
    time=request.form["time"]
    code = codes.getCode()
    print(code)
    timer.start_multiple_timers({code:int(time)})
    return code

if __name__ == '__main__':
    app.run(host='0.0.0.0')