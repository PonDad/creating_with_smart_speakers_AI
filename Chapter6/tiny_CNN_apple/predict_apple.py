from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

rgb_image = './images/green_apple_101.jpg'
#rgb_image = 'images/red_apple_101.jpg'

model_path = './trained_models/tiny_CNN_apple.h5
model = load_model(model_path)

apple_labels = ['青りんご','赤りんご']

load_img = image.load_img(rgb_image, target_size=(32, 32))
x = image.img_to_array(load_img)
x = np.expand_dims(x, axis=0) / 255

apple_predict = model.predict(x)
if apple_predict < 0.5:
    apple_text = apple_labels[0]
elif apple_predict >= 0.5:
    apple_text = apple_labels[1]
print(apple_text, apple_predict[0][0])
