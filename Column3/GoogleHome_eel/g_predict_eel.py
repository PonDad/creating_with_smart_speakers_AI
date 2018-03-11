import sys, os, json
import numpy as np
from flask import Flask,request, make_response, jsonify, render_template
from flask_assistant import Assistant, ask, tell
from picamera import PiCamera
from time import sleep
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

app = Flask(__name__)
assist = Assistant(app, '/')

rgb_image = './images/apple.jpg'
model_path = './trained_models/tiny_CNN_eel.h5'
apple_labels = ['チンアナゴ','ニシキアナゴ']

picamera = PiCamera()
model = load_model(model_path)

@assist.action('Default Welcome Intent')
def greet_and_start():
    return ask('チン、チン、チンアナ〜ゴ。チンアナゴとニシキアナゴを見分けたい時はハイチーズって言ってね')

@assist.action('CameraIntent')
def camera():
    picamera.resolution = (150, 150)
    picamera.start_preview()
    sleep(0.5)
    picamera.capture(rgb_image)
    picamera.stop_preview()
    return ask('カシャッ')

@assist.action('eelIntent')
def what():
    load_img = image.load_img(rgb_image, target_size=(32, 32))
    x = image.img_to_array(load_img)
    x = np.expand_dims(x, axis=0) / 255

    apple_predict = model.predict(x)
    if apple_predict < 0.5:
        print(apple_labels[0], apple_predict[0][0])
        return tell('これは{}ですね。チン、チン、チンアナ〜ゴ。'.format(apple_labels[0]))

    elif apple_predict >= 0.5:
        print(apple_labels[1], apple_predict[0][0])
        return tell('これは{}ですね。チン、チン、チンアナ〜ゴじゃなかった。'.format(apple_labels[1]))
    else:
        print('なにアナゴかよくわかりません')
        return ask('なにアナゴかよくわかりません')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
