import numpy as np
np.random.seed(1337)
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, classification_report

data = genfromtxt ('D:/bookFiles/data_banknote_authentication. txt', delimiter=',', skip_header=False)
# print(data)
labels = data[:, -1]
features = data[:, 0:4]
# print(features)
x = features
y = labels
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=42)
# print(len(x_train), len(x_test))

scaler_object = MinMaxScaler()
scaler_object.fit(x_train)
scaled_x_train = scaler_object.transform(x_train)
# print (scaled_x_train)
scaled_x_test = scaler_object.transform(x_test)