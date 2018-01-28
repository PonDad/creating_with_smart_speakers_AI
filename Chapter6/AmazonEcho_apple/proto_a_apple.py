import sys, os, json
import numpy as np
from flask import Flask,request, make_response, jsonify, render_template
from flask_ask import Ask, statement, question
from picamera import PiCamera
from time import sleep
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

app = Flask(__name__)
ask = Ask(app, '/')

rgb_image = './images/apple.jpg'
model_path = './trained_models/tiny_CNN_apple.h5'
apple_labels = ['青りんご','赤りんご']

picamera = PiCamera()
model = load_model(model_path)

@ask.launch
def launched():
    return question('お腹すいた。りんごが食べたい。')

@ask.intent('CameraIntent')
def camera():
    picamera.resolution = (150, 150)
    picamera.start_preview()
    sleep(0.5)
    picamera.capture(rgb_image)
    picamera.stop_preview()
    return question('カシャッ')

@ask.intent('WhatIntent')
def what():
    load_img = image.load_img(rgb_image, target_size=(32, 32))
    x = image.img_to_array(load_img)
    x = np.expand_dims(x, axis=0) / 255

    apple_predict = model.predict(x)
    if apple_predict < 0.5:
        print(apple_labels[0], apple_predict[0][0])
        return question('これは{}ですね。わたし青りんご嫌い。'.format(apple_labels[0]))

    elif apple_predict >= 0.5:
        print(apple_labels[1], apple_predict[0][0])
        return question('これは{}ですね。わーい、赤りんご大好き。'.format(apple_labels[1]))
    else:
        print('なにりんごかよくわかりません')
        return question('なにりんごかよくわかりません')

@ask.session_ended
def session_ended():
    return "{}", 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
