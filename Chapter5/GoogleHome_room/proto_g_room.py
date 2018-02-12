import json
import requests
from flask import Flask, render_template, request
from flask_assistant import Assistant, ask, tell
from proto_time_db import start, stop
from proto_eremote import temp_on, temp_off,hum_on, hum_off
from tinydb import TinyDB,Query

db = TinyDB("db.json")
sensor = Query()

app = Flask(__name__)
assist = Assistant(app, '/')

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

@assist.action('Default Welcome Intent')
def greet_and_start():
    text = "はいプロトです。本を読む時は、読書をはじめるよって言ってね。"
    return ask(text)

@assist.action('readingStart')
def readingStart():
    start()
    t = float(db.search(sensor.key == "temp")[0]["value"])
    h = int(db.search(sensor.key == "hum")[0]["value"])
    print("temp:" + str(t),"hum:" + str(h))
    if t < 20 and h < 60 :
        text = "ちょっと寒いですね、暖房を点けますか？"
        return ask("読書をはじめます。" + text)
    else:
        text = "お部屋の温度はちょうどいいですね。"
        return tell("読書をはじめます。" + text)

@assist.action('readingEnd')
def readingEnd():
    r = stop()
    p1 = db.search(sensor.key == "temp_power")[0]["value"]
    p2 = db.search(sensor.key == "hum_power")[0]["value"]
    if p1 == 1:
        text = "暖房を消しますか？"
        return ask('読書の時間は' + str(r) + 'でした。' + text)
    else:
        return tell('読書の時間は' + str(r) + 'でした。お疲れさまでした。')

@assist.action('onIntent')
def on():
    temp_on()
    db.update({"value":1},sensor.key == "temp_power")

    h = int(db.search(sensor.key == "hum")[0]["value"])
    if h < 60:
        hum_on()
        db.update({"value":1},sensor.key == "hum_power")
    else:
        pass
    return tell('暖房を入れました。快適に読書を楽しんでね。')

@assist.action('offIntent')
def off():
    temp_off()
    db.update({"value":0},sensor.key == "temp_power")

    p2 = db.search(sensor.key == "hum_power")[0]["value"]
    if p2 == 1:
        hum_off()
        db.update({"value":0},sensor.key == "hum_power")
    else:
        pass
    return tell('暖房を消しました。お疲れさまでした。')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
