import json
import requests
from flask import Flask, render_template, request
from flask_assistant import Assistant, ask, tell
from eremote_kuratas import fire, right, left, filling

app = Flask(__name__)
assist = Assistant(app, '/')

@assist.action('Default Welcome Intent')
def greet_and_start():
    text = "ウェルカム、トゥ、クラタス"
    return ask(text)

@assist.action('fireIntent')
def fired():
    fire()
    return ask('ファイヤー')

@assist.action('rightIntent')
def turn_right():
    right()
    return ask('右')

@assist.action('leftIntent')
def turn_left():
    left()
    return ask('左')

@assist.action('fillIntent')
def filling_enagy():
    filling()
    return ask('充填しました')

@assist.action('endIntent')
def end():
    return tell('グッバイ')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
