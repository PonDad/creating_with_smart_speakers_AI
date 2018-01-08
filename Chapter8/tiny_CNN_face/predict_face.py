from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

#rgb_image = './images/test_mika/test_mika_6.jpg'
rgb_image = './images/test_rika/test_rika_6.jpg'

model = load_model('./trained_models/tiny_CNN_face.h5')

face_labels = ['ミカ','リカ']

img = image.load_img(rgb_image, target_size=(32, 32))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0) / 255

face_predict = model.predict(x)
if face_predict < 0.5:
    face_text = face_labels[0]
elif face_predict >= 0.5:
    face_text = face_labels[1]
print(face_text, face_predict[0][0])
