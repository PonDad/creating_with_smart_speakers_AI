from flask import Flask
from flask_assistant import Assistant, ask, tell

app = Flask(__name__)
assist = Assistant(app)

red_price = 90
green_price =120

def checkout(x, y):
    checkout = x * red_price + y * green_price
    return checkout

@assist.action('Default Welcome Intent')
def greet_and_start():
    speech = "いらっしゃい、赤りんごと青りんごがおすすめですよ。"
    return ask(speech)

@assist.action('CalcIntent',mapping={'num_1': 'number_1','num_2': 'number_2','red_apple': 'list_of_red','green_apple': 'list_of_green'})
def calc(num_1,num_2,red_apple,green_apple):
    if not red_apple == "赤りんご":
        checkout_all = int(num_2) * green_price
        speech = '{}{}個でお会計{}円になります'.format(green_apple,num_2,checkout_all)
        return tell(speech)
    elif not green_apple == "青りんご":
        checkout_all = int(num_1) * red_price
        speech = '{}{}個でお会計{}円になります'.format(red_apple,num_1,checkout_all)
        return tell(speech)
    else:
        checkout_all = checkout(int(num_1) ,int(num_2))
        speech = '{}{}個と{}{}個でお会計{}円になります'.format(red_apple,num_1,green_apple,num_2,checkout_all)
        return tell(speech)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
