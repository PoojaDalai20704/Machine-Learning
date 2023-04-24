import numpy as np import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_s plit
import matplotlib.pyplot as plt data = load_iris()
X=data.data y=data.target
y = pd.get_dummies(y).values y[:3]
X_train, X_test, y_train, y_test = train_test_sp lit(X, y, test_size=20, random_state=4)
learning_rate = 0.1
iterations = 5000 N = y_train.size input_size = 4
hidden_size = 2
output_size = 3
results = pd.DataFrame(columns=["mse", "accuracy"])
 

def sigmoid(x):
return 1 / (1 + np.exp(-x))
def mean_squared_error(y_pred, y_true): return ((y_pred -
 
y_true)**2).sum() / (2*y_pred.size) def accuracy(y_pred, y_true):
acc = y_pred.argmax(axis=1) == y_true.argmax (axis=1)
return acc.mean()
for itr in range(iterations):
 
Z1 = np.dot(x_train, W1) A1 = sigmoid(Z1)
Z2 = np.dot(A1, W2) A2 = sigmoid(Z2)
mse = mean_squared_error(A2, y_train) acc = accuracy(A2, y_train)
results=results.append({"mse":mse, "accuracy ":acc},ignore_index=True )
E1 = A2 - y_train
dW1 = E1 * A2 * (1 - A2)
E2 = np.dot(dW1, W2.T) dW2 = E2 * A1 * (1 - A1)
W2_update = np.dot(A1.T, dW1) / N W1_update = np.dot(x_train.T, dW2) / N W2 = W2 - learning_rate * W2_update
W1 = W1 - learning_rate * W1_update results.mse.plot(title="Mean Squared Error") results.accuracy.plot(title="Accuracy")
Z1 = np.dot(x_test, W1) A1 = sigmoid(Z1)
Z2 = np.dot(A1, W2) A2 = sigmoid(Z2)
acc = accuracy(A2, y_test) print("Accuracy: {}".format(acc))
