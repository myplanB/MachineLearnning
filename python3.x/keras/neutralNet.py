from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras import backend
from keras.callbacks import LearningRateScheduler, TensorBoard

backend.set_image_data_format('channels_first')


def create_model1(num_pixels, num_classes):
    model = Sequential()
    model.add(Dense(units=64, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
    model.add(Dense(units=num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def create_model2():
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5, 5), input_shape=(1, 28, 28), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(rate=0.2))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=10, activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model


def net1():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    seed = 7
    np.random.seed(seed)

    # x_train (6000,28,28)
    num_pixel = x_train.shape[1] * x_train.shape[2]
    # 将每张图片转化成一列数据
    x_train = x_train.reshape(x_train.shape[0], num_pixel).astype('float32')
    x_test = x_test.reshape(x_test.shape[0], num_pixel).astype('float32')

    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)

    x_train = x_train / 255
    x_test = x_test / 255
    print(type(x_train))

    num_classes = y_test.shape[1]
    print('num_classes: {}'.format(num_classes))

    model = create_model1(num_pixels=num_pixel, num_classes=num_classes)
    model.fit(x_train, y_train, batch_size=32, epochs=10)
    score = model.evaluate(x_train, y_train, batch_size=32)
    print(score[1])


def net2():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    seed = 7
    np.random.seed(seed)

    x_train = x_train.reshape(x_train.shape[0], 1, 28, 28).astype('float32')
    x_test = x_test.reshape(x_test.shape[0], 1, 28, 28).astype('float32')

    x_train = x_train / 255
    x_test = x_test / 255

    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)

    model = create_model2()
    model.fit(x_train, y_train, epochs=10, batch_size=200, verbose=1, callbacks=[LearningRateScheduler(scheduler),TensorBoard(log_dir='./logs')])
    score = model.evaluate(x_test, y_test, verbose=0)
    print(score[1])


def scheduler(epoch):
    if epoch <= 60:
        return 0.05
    elif epoch <= 120:
        return 0.01
    elif epoch <= 160:
        return 0.002
    else:
        return 0.0004


if __name__ == '__main__':
    net2()
