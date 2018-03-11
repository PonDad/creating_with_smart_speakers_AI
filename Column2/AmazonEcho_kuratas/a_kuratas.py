import json
import requests
from flask import Flask, render_template, request
from flask_ask import Ask, statement, question
from eremote_kuratas import fire, right, left, filling

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    text = "ウェルカム、トゥ、クラタス"
    return question(text)

@ask.intent('fireIntent')
def fired():
    fire()
    return question('ファイヤー')

@ask.intent('rightIntent')
def turn_right():
    right()
    return question('右')

@ask.intent('leftIntent')
def turn_left():
    left()
    return question('左')

@ask.intent('fillIntent')
def filling_enagy():
    filling()
    return question('充填しました')

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
