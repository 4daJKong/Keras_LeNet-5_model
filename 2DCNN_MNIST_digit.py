import keras
import tensorflow as tf
import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt
from numpy import float32


(X_train, y_train), (X_test, y_test) = mnist.load_data()

#digits show#
'''
fig, ax = plt.subplots(5, 5, figsize=(8,8))
for i, ax in enumerate(ax.flat):   
    ax.imshow(X_train[i], cmap='Greys')
    ax.set_title("Digit:{}".format(y_train[i]))
fig.tight_layout()
plt.show()
'''

#resize images and normalize
X_train = np.expand_dims(X_train, axis=-1)
X_train = X_train.astype(float32)/255
X_train = tf.image.resize(X_train, [32,32])

X_test = np.expand_dims(X_test, axis=-1)
X_test = X_test.astype(float32)/255
X_test = tf.image.resize(X_test, [32,32])

num_category = 10
y_train = keras.utils.np_utils.to_categorical(y_train, num_category)
y_test = keras.utils.np_utils.to_categorical(y_test, num_category)



#LeNet-5 model#
model =keras.Sequential([
   keras.layers.Conv2D(6, 5, activation = 'relu', input_shape= (32, 32, 1)),
   keras.layers.AveragePooling2D(2),
   keras.layers.Conv2D(16, 5, activation = 'relu'),
   keras.layers.AveragePooling2D(2),
   keras.layers.Flatten(),
   keras.layers.Dense(120, activation='relu'),
   keras.layers.Dense(84, activation='relu'),
   keras.layers.Dense(10, activation='softmax')
])

print(model.summary())

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

model.log = model.fit(x = X_train, y = y_train, 
                batch_size = 200,
                epochs= 10,
                verbose= 1)
score = model.evaluate(X_test, y_test, verbose= 0)
print('test loss:', score[0])
print('test accuracy:', score[1])

model.save('lenet-5.h5')
test_model = keras.models.load_model('lenet-5.h5')




