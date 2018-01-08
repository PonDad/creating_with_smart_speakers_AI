from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np

rgb_image = './images/mika_110.jpg'

emotion_model_path = './trained_models/fer2013_mini_XCEPTION.102-0.66.hdf5'

emotion_labels = ({0:'angry',1:'disgust',2:'fear',3:'happy',
        4:'sad',5:'surprise',6:'neutral'})

model = load_model(emotion_model_path, compile=False)

load_img = image.load_img(rgb_image, grayscale=True , target_size=(64, 64))
x = image.img_to_array(load_img)
x = np.expand_dims(x, axis=0) / 255

emotion_label_arg = np.argmax(model.predict(x))
emotion_text = emotion_labels[emotion_label_arg]
emotion_ratio = np.max(model.predict(x))
print(emotion_text,emotion_ratio)
