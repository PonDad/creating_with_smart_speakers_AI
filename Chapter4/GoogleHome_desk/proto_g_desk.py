import json
import requests
from flask import Flask, render_template, request
from flask_assistant import Assistant, ask, tell
from proto_blight import blight_result
from proto_time import start, stop
from proto_hue import hue_on, hue_off

app = Flask(__name__)
assist = Assistant(app, '/')

@app.route("/blight", methods=['POST'])
def blight():
    result = request.data.decode()
    data = {
    "blight_lux":int(result)
    }
    file = open("blight.json", "w")
    json.dump(data, file)
    return result

@assist.action('Default Welcome Intent')
def greet_and_start():
    result = blight_result()
    text = "はいプロトです。宿題をはじめる時は、宿題をはじめるよって言ってね。"
    return ask(text)

@assist.action('stydyStart')
def studyStart():
    start()
    result = blight_result()
    print("blight:" + str(result) + "lux")
    if result < 500:
        text = "手もとが暗いですね。明かりをつけますか？"
        return ask("宿題をはじめます。" + text)
    else:
        return tell("宿題をはじめます。")

@assist.action('studyEnd')
def studyEnd():
    result_time = stop()

    result = blight_result()
    print("blight:" + str(result) + "lux")

    if 500 <= result:
        text = "明かりを消しますか？"
        return ask('机に向かった時間は' + str(result_time) + 'でした。' + text)
    else:
        return tell('机に向かった時間は' + str(result_time) + 'でした。お疲れさまでした。')

@assist.action('onIntent')
def on():
    hue_on()
    return tell('最適な明かりで設定しました。宿題頑張ってね。')

@assist.action('offIntent')
def off():
    hue_off()
    result = stop()
    return tell('明かりを消しました。お疲れさまでした。')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
