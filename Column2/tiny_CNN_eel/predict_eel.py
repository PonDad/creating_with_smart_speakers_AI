from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

#rgb_image = './images/chin_101.jpg'
#rgb_image = './images/nishiki_101.jpg'
#rgb_image = './images/chin_102.jpg'
#rgb_image = './images/nishiki_102.jpg'
#rgb_image = './images/chin_103.jpg'
#rgb_image = './images/nishiki_103.jpg'
#rgb_image = './images/chin_104.jpg'
#rgb_image = './images/nishiki_104.jpg'
#rgb_image = './images/chin_105.jpg'
#rgb_image = './images/nishiki_105.jpg'
#rgb_image = './images/sumida_0.jpg'
#rgb_image = './images/sumida_1.jpg'
#rgb_image = './images/amazon_0.jpg'
rgb_image = './images/amazon_1.jpg'

model_path = './trained_models/tiny_CNN_eel.h5'
model = load_model(model_path)
eel_labels = ['チンアナゴ','ニシキアナゴ']

load_img = image.load_img(rgb_image, target_size=(32, 32))
x = image.img_to_array(load_img)
x = np.expand_dims(x, axis=0) / 255

eel_predict = model.predict(x)
if eel_predict < 0.5:
    eel_text = eel_labels[0]
elif eel_predict >= 0.5:
    eel_text = eel_labels[1]
print(eel_text, eel_predict[0][0])
