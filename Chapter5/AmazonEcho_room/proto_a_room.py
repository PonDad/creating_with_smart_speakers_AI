import json
import requests
from flask import Flask, render_template, request
from flask_ask import Ask, statement, question
from proto_time_db import start, stop
from proto_eremote import temp_on, temp_off,hum_on, hum_off
from tinydb import TinyDB,Query

db = TinyDB("db.json")
sensor = Query()

app = Flask(__name__)
ask = Ask(app, '/')

@app.route("/temp", methods=['POST'])
def temp():
    temp = request.data.decode()
    db.update({"value":temp},sensor.key == "temp")
    return temp

@app.route("/hum", methods=['POST'])
def hum():
    hum = request.data.decode()
    db.update({"value":hum},sensor.key == "hum")
    return hum

@ask.launch
def launched():
    text = "はいプロトです。本を読む時は、読書をはじめるよって言ってね。"
    return question(text)

@ask.intent('readingStart')
def readingStart():
    start()
    t = float(db.search(sensor.key == "temp")[0]["value"])
    h = int(db.search(sensor.key == "hum")[0]["value"])
    print("temp:" + str(t),"hum:" + str(h))
    if t < 20 and h < 60 :
        text = "ちょっと寒いですね、暖房を点けますか？"
        return question("読書をはじめます。" + text)
    else:
        text = "お部屋の温度はちょうどいいですね。"
        return statement("読書をはじめます。" + text)

@ask.intent('readingEnd')
def readingEnd():
    r = stop()
    p1 = db.search(sensor.key == "temp_power")[0]["value"]
    p2 = db.search(sensor.key == "hum_power")[0]["value"]
    if p1 == 1:
        text = "暖房を消しますか？"
        return question('読書の時間は' + str(r) + 'でした。' + text)
    else:
        return statement('読書の時間は' + str(r) + 'でした。お疲れさまでした。')

@ask.intent('onIntent')
def on():
    temp_on()
    db.update({"value":1},sensor.key == "temp_power")

    h = int(db.search(sensor.key == "hum")[0]["value"])
    if h < 60:
        hum_on()
        db.update({"value":1},sensor.key == "hum_power")
    else:
        pass
    return statement('暖房を入れました。快適に読書を楽しんでね。')

@ask.intent('offIntent')
def off():
    temp_off()
    db.update({"value":0},sensor.key == "temp_power")

    p2 = db.search(sensor.key == "hum_power")[0]["value"]
    if p2 == 1:
        hum_off()
        db.update({"value":0},sensor.key == "hum_power")
    else:
        pass
    return statement('暖房を消しました。お疲れさまでした。')

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
