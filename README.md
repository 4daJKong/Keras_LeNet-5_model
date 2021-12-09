# Keras_LeNet-5_model
A simple CNN model based on Keras API
## Introduction
I followed and implemented the LeNet-5 CNN architecture by Keras API, then trained the model by MNIST dataset. The test loss is 0.035 and the test accuracy is 0.989 after evaluating.(For more specific training and testing process, it is on 2DCNN_MNIST_digit.py) After that, I serach some digits verification code on the internet and decide to get further result on the performance of my model. Unfortunately, the performance is not good. I guess the main problem is the difference between MNIST and other digits in their art styles. 
## The architecture and parameters of LeNet-5 CNN
![lenet-5_arch](https://user-images.githubusercontent.com/34623632/145355500-31fce43f-47a8-49a2-9758-73a9e3742768.png)

_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 28, 28, 6)         156

 average_pooling2d (AverageP  (None, 14, 14, 6)        0
 ooling2D)

 conv2d_1 (Conv2D)           (None, 10, 10, 16)        2416

 average_pooling2d_1 (Averag  (None, 5, 5, 16)         0
 ePooling2D)

 flatten (Flatten)           (None, 400)               0

 dense (Dense)               (None, 120)               48120

 dense_1 (Dense)             (None, 84)                10164

 dense_2 (Dense)             (None, 10)                850

=================================================================
Total params: 61,706
Trainable params: 61,706
Non-trainable params: 0
_________________________________________________________________
