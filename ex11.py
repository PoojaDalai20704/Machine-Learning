import warnings warnings.filterwarnings('ignore') import numpy as np
import matplotlib.pyplot as plt import keras
from keras.datasets import mnist
from keras.models import Sequential,model_from_j

from keras.layers import Dense
from keras.optimizers import RMSprop import pylab as plt
num_classes = 10
epochs = 2
(x_train, y_train), (x_test, y_test) = mnist.loa
 
d_data()
mnist
x_train = x_train.reshape(60000, 784) x_test = x_test.reshape(10000, 784) x_train = x_train.astype('float32') x_test = x_test.astype('float32') x_train /= 255
x_test /= 255
print(x_test.shape[0], 'test samples')
y_train = keras.utils.to_categorical(y_train, nu m_classes)
y_test = keras.utils.to_categorical(y_test, num_ classes)
first_layer_size = 32 model = Sequential()'))
 
model.add(Dense(first_layer_size, activation='si gmoid', input_shape=(784,))) model.add(Dense(32, activation='tanh')) model.add(Dense(32, activation='tanh')) model.add(Dense(32, activation='tanh')) model.add(Dense(num_classes, activation='softmax

w = []
for layer in model.layers:
weights = layer.get_weights() w.append(weights)
layer1 = np.array(w[0][0])
print("Shape of First Layer",layer1.shape) print("Visualization of First Layer") fig=plt.figure(figsize=(12, 12))
columns = 8
rows = int(first_layer_size/8)
for i in range(1, columns*rows +1): fig.add_subplot(rows, columns, i) plt.imshow(layer1[:,i-1].reshape(28,28),cmap='gray') plt.show()
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
epochs
history = model.fit(x_train,y_train,
batch_size=batch_size, epochs=5,
verbose=1)
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0]) print('Test accuracy:', score[1]) w = []
for layer in model.layers:
weights = layer.get_weights() w.append(weights)
layer1 = np.array(w[0][0])
 
print("Shape of First Layer",layer1.shape) print("Visualization of First Layer") fig=plt.figure(figsize=(12, 12))
columns = 8
rows = int(first_layer_size/8)
for i in range(1, columns*rows +1): fig.add_subplot(rows, columns, i) plt.imshow(layer1[:,i-1].reshape(28,28),cmap='gray') plt.show()
plt.imshow(x_test[88:89].reshape(28,28),cmap='gr ay')
plt.show() import cv2
import numpy as np
from matplotlib import pyplot as plt
image_bgr = cv2.imread('/content/drive/MyDrive/2 0230331_164204.jpg', cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BG R2RGB)
plt.imshow(image_rgb), plt.axis("off") plt.show()
