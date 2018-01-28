import sys, os, json
import numpy as np
from flask import Flask,request, make_response, jsonify, render_template
from flask_assistant import Assistant, ask, tell
from picamera import PiCamera
from time import sleep
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import cv2

app = Flask(__name__)
assist = Assistant(app, '/')

rgb_image = './images/face.jpg'
model_path = './trained_models/tiny_CNN_face.h5'
cascade_path = "./trained_models/haarcascade_frontalface_alt2.xml"
face_labels = ['ミカ','リカ']

picamera = PiCamera()
model = load_model(model_path)

@assist.action('Default Welcome Intent')
def greet_and_start():
    return ask('写真を撮る時はハイチーズって言ってね。')

@assist.action('CameraIntent')
def camera():
    picamera.resolution = (150, 150)
    picamera.start_preview()
    picamera.capture(rgb_image)
    sleep(0.5)
    picamera.stop_preview()

    cv_image = cv2.imread(rgb_image)

    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)

    facerect = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=2, minSize=(10, 10))

    if len(facerect) > 0:
        for rect in facerect:
            x, y, w, h = rect[0], rect[1], rect[2], rect[3]
            dst =  cv_image[y:y + h, x:x + w]
        cv2.imwrite(rgb_image, dst)
        print("crop")

    else:
        print("none")
    return ask('カシャッ')

@assist.action('WhoIntent')
def who():
    load_img = image.load_img(rgb_image, target_size=(32, 32))
    x = image.img_to_array(load_img)
    x = np.expand_dims(x, axis=0) / 255

    face_predict = model.predict(x)
    if face_predict < 0.5:
        print(face_labels[0], face_predict[0][0])
        return tell('あなたは{}ちゃんですね。'.format(face_labels[0]))
    elif face_predict >= 0.5:
        print(face_labels[1], face_predict[0][0])
        return tell('あなたは{}ちゃんですね。'.format(face_labels[1]))
    else:
        print('だれ？')
        return ask('だれだかよくわかりません')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
