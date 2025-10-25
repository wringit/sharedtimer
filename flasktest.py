from flask import Flask, redirect, url_for, render_template, request # Flask class which will be instantiated
import time
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/timers/<code>')
def timer(code):
    return code


if __name__ == '__main__':
    app.run()
    time.sleep(1)
    