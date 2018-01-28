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
import random
# hue の操作不要の場合削除してください
import proto_hue_emotion as hue

app = Flask(__name__)
assist = Assistant(app, '/')

rgb_image = './images/emotion.jpg'
emotion_model_path = './trained_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
cascade_path = "./trained_models/haarcascade_frontalface_alt2.xml"

emotion_labels = ({0:'angry',1:'disgust',2:'fear',3:'happy', 4:'sad',5:'surprise',6:'neutral'})

emotion_phrase =({
0:["やる気充分","熱い","格好いい"],
1:["あなたらしい","クール","個性的"],
2:["慎重","冷静","謙虚"],
3:["最高の気分","元気","明るい"],
4:["感無量","胸が一杯","涙がでそう"],
5:["びっくり","サプライズ","最高"],
6:["自然体","肩の力が抜けていい感じ","ナチュラル"]
})

picamera = PiCamera()
# compile=False　で指定してください
model = load_model(emotion_model_path, compile=False)

@assist.action('Default Welcome Intent')
def greet_and_start():
    return ask('今日は大切な日ですね。忘れ物はないですか？ちょっと顔をみせてください。')

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

@assist.action('EmotionIntent')
def emotion():
    load_img = image.load_img(rgb_image, grayscale=True, target_size=(64, 64))
    x = image.img_to_array(load_img)
    x = np.expand_dims(x, axis=0) / 255

    emotion_label_arg = np.argmax(model.predict(x))
    emotion_text = emotion_labels[emotion_label_arg]
    emotion_ratio = np.max(model.predict(x))
    emotion_phrase_rand = random.choice(emotion_phrase[emotion_label_arg])
    # hue の操作不要の場合削除してください
    hue.change_light(emotion_label_arg)
    print(emotion_text,emotion_ratio)
    return tell('{}ですね。いってらっしゃい。'.format(emotion_phrase_rand))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
