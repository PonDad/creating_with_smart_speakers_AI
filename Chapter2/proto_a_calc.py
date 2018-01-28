from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('プロトです。今は足し算と引き算がしたい気分です。')

@ask.intent('calcIntent', convert={'firstNum': int, 'secondNum': int, 'calcAdd': str, 'calcSub': str})
def add(firstNum, secondNum, calcAdd, calcSub):
    if calcAdd:
        answer = firstNum + secondNum
        calc = calcAdd
    elif calcSub:
        answer = firstNum - secondNum
        calc = calcSub
    return statement('{} {} {} は {} だよ'.format(firstNum, calc, secondNum, answer))

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
