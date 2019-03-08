from keras.models import Sequential,Model
from keras.layers import Dense,Activation,Dropout,Input
import keras
import numpy as np
from keras.optimizers import SGD

def create_model(num_classes):
    model = Sequential()
    model.add(Dense(units=32,activation='relu',kernel_initializer='normal',input_dim=48*48))
    model.add(Dense(units=64,activation='relu',kernel_initializer='normal'))
    model.add(Dense(units=128,activation='relu',kernel_initializer='normal'))
    model.add(Dense(units=num_classes,kernel_initializer='normal',activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model

if __name__ == '__main__':
    # 读取数据
    new_data = []
    labels = []
    with open('data/fer2013.csv',encoding='utf-8') as f:
        lines = f.readlines()
        cnt = 0
        for line in lines:
            line = line.strip()
            cnt += 1
            if cnt == 1:
                continue
            items = line.strip().split(",")
            label = items[0]
            data = items[1]
            data = data.split(" ")
            data = [int(i) for i in data]
            new_data.append(np.array(data)/255)
            labels.append(label)

        data = np.array(new_data)
        labels = [int(i) for i in labels]
        labels = np.array(labels)
        print(len(labels))

        # 训练集和测试集
        x_train = data[:30000]
        y_train = labels[:30000]
        y_train = keras.utils.to_categorical(y_train,7)

        x_test = data[30000:]
        y_test =labels[30000:]
        y_test = keras.utils.to_categorical(y_test,7)


        model = create_model(7)
        model.fit(x_train,y_train,epochs=10000,batch_size=200)
        score = model.evaluate(x_test,y_test,batch_size=200)
        print(score)

