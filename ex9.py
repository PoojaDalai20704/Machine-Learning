import numpy as np import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_ split
import matplotlib.pyplot as plt data = load_iris()
X=data.data y=data.target
y = pd.get_dummies(y).values y[:3]
X_train, X_test, y_train, y_test = train_test_s plit(X, y, test_size=20, random_state=4)
learning_rate = 0.1
iterations = 5000 N = y_train.size input_size = 4
hidden_size = 2
output_size = 3
results = pd.DataFrame(columns=["mse", "accuracy"])
 

for itr in range(iterations): Z1 = np.dot(x_train, W1) A1 = sigmoid(Z1)
Z2 = np.dot(A1, W2) A2 = sigmoid(Z2)
mse = mean_squared_error(A2, y_train) acc = accuracy(A2, y_train)
results=results.append({"mse":mse, "accuracy":acc},ignore_index=True )
 
E1 = A2 - y_train
dW1 = E1 * A2 * (1 - A2)
E2 = np.dot(dW1, W2.T) dW2 = E2 * A1 * (1 - A1)
W2_update = np.dot(A1.T, dW1) / N W1_update = np.dot(x_train.T, dW2) / N W2 = W2 - learning_rate * W2_update
W1 = W1 - learning_rate * W1_update results.mse.plot(title="Mean Squared Error") import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar100 from tensorflow.keras.models import Sequential from tensorflow.keras.layers import Dense, Drop
out, BatchNormalization
from tensorflow.keras.callbacks import EarlySto pping
(x_train, y_train), (x_test, y_test) = cifar100.load_data()
x_train = x_train.astype('float32') / 255.0 x_test = x_test.astype('float32') / 255.0 num_classes = 100
y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)
model = Sequential([

tf.keras.layers.Flatten(input_shape=(32, 32, 3)),

tf.keras.layers.Dense(512, activation='relu'), tf.keras.layers.BatchNormalization(), tf.keras.layers.Dropout(0.2), tf.keras.layers.Dense(256, activation='relu'),
tf.keras.layers.BatchNormalization(), tf.keras.layers.Dropout(0.2),
 
tf.keras.layers.Dense(num_classes, activatio n='softmax')])
model.compile(optimizer='adam', loss='categorica l_crossentropy', metrics=['accuracy'])
early_stop = EarlyStopping(monitor='val_loss', p atience=5)
history = model.fit(x_train, y_train, epochs=50, batch_size=64, validation_split=0.2, callbacks=[ea
rly_stop])
test_loss, test_acc = model.evaluate(x_test, y_t est)
print("Test accuracy:", test_acc)
