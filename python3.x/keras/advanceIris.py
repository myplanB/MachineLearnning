from sklearn import datasets
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import model_from_json

def create_model(optimizer='rmsprop',init='glorot_uniform'):
    model = Sequential()
    model.add(Dense(units=4,input_dim=4,activation='relu',kernel_initializer=init))
    model.add(Dense(units=10,activation='relu',kernel_initializer=init))
    model.add(Dense(units=3,activation='softmax',kernel_initializer=init))
    model.compile(loss='categorical_crossentropy',optimizer=optimizer,metrics=['accuracy'])
    return model

if __name__ == '__main__':
    dataset = datasets.load_iris()

    x = dataset.data
    y = dataset.target

    # one-hot编码
    y_labels = to_categorical(y,num_classes=3)
    seed = 7
    np.random.seed(seed)

    model = create_model()
    model.fit(x,y_labels,verbose=1)

    scores = model.evaluate(x,y_labels,verbose=1)
    print('{}-{}'.format(model.metrics_names[1],scores[1]))

    # 保存json文件
    model_json = model.to_json()
    with open('model.json','w') as f:
        f.write(model_json)

    # 保存权重文件
    model.save_weights('model.json.h5')

    # 从JSON文件中加载模型
    with open('model.json','r') as f:
        model_json = f.read()

    new_model = model_from_json(model_json)
    new_model.load_weights('model.json.h5')
    new_model.compile(loss='categorical_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

    scores = new_model.evaluate(x,y_labels,verbose=0)
    print('{},  {}'.format(model.metrics_names[1],scores[1]))