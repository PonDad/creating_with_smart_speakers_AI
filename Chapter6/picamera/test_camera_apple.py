from flask import Flask
from picamera import PiCamera
from time import sleep

app = Flask(__name__)

picamera = PiCamera()
rgb_image = './images/apple.jpg'

@app.route('/')
def camera():
    picamera.resolution = (150, 150)
    picamera.start_preview()
    picamera.capture(rgb_image)
    sleep(0.5)
    picamera.stop_preview()
    return

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
