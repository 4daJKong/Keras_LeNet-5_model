from typing import Mapping
import keras
import cv2
import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

os.chdir('D:\Python_ex\lenet_5')

test_model = keras.models.load_model('lenet-5.h5')
file_pathname = './digit_test'

fig = plt.figure()
cnt = 1

for filename in os.listdir(file_pathname):
    img = cv2.imread(file_pathname + '\\' + filename)
    
    fig.add_subplot(5,4,cnt)
    plt.imshow(img)
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.expand_dims(img, axis=-1)
    img = img.astype(np.float32)/255
    img = tf.image.resize(img, [32,32])
    img = tf.expand_dims(img, axis = 0)
    predict_value = test_model.predict(img)
    digit = np.argmax(predict_value)
    
    plt.title("Predict_Digit:{}".format(digit))
    plt.axis('off')
    cnt += 1

plt.show()

  


    
    
