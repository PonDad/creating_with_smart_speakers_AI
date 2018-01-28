import json
import requests
from flask import Flask, render_template, request
from flask_ask import Ask, statement, question
from proto_blight import blight_result
from proto_time import start, stop
from proto_hue import hue_on, hue_off

app = Flask(__name__)
ask = Ask(app, '/')

@app.route("/blight", methods=['POST'])
def blight():
    result = request.data.decode()
    data = {
    "blight_lux":int(result)
    }
    file = open("blight.json", "w")
    json.dump(data, file)
    return result

@ask.launch
def launched():
    result = blight_result()
    text = "はいプロトです。宿題をはじめる時は、宿題をはじめるよって言ってね。"
    return question(text)

@ask.intent('stydyStart')
def studyStart():
    start()
    result = blight_result()
    print("blight:" + str(result) + "lux")
    if result < 500:
        text = "手もとが暗いですね。明かりをつけますか？"
    else:
        text = ""
    return question("宿題をはじめます。" + text)

@ask.intent('studyEnd')
def studyEnd():
    result_time = stop()

    result = blight_result()
    print("blight:" + str(result) + "lux")

    if 500 <= result:
        text = "明かりを消しますか？"
        return question('机に向かった時間は' + str(result_time) + 'でした。' + text)
    else:
        return statement('机に向かった時間は' + str(result_time) + 'でした。お疲れさまでした。')

@ask.intent('onIntent')
def on():
    hue_on()
    return statement('最適な明かりで設定しました。宿題頑張ってね。')

@ask.intent('offIntent')
def off():
    hue_off()
    result = stop()
    return statement('明かりを消しました。お疲れさまでした。')

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
