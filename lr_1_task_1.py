# -*- coding: utf-8 -*-
"""LR_1_task_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1adLiBd4qsX1spubp-LLSsa44HbJ7_3Ib
"""

import numpy as np
from sklearn import preprocessing

input_data = np.array([[5.1, -2.9, 3.3],
[-1.2, 7.8, -6.1],
[3.9, 0.4, 2.1],
[7.3, -9.9, -4.5]])

# Бінаризація даних
data_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data)
print("Binarized data:\n" , data_binarized)

print("\nBEFORE: ")
print("Mean =", input_data.mean(axis=0))
print("Std deviation =", input_data.std(axis=0))

# Виключення середнього
data_scaled = preprocessing.scale(input_data)
print("\nAFTER: ")
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis=0))

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nМin max scaled data:\n", data_scaled_minmax)

data_normalized_l1 = preprocessing.normalize(input_data,norm='l1')
data_normalized_l2 = preprocessing.normalize(input_data,norm='l2')
print("\nl1 normalized data:\n", data_normalized_l1)
print("\nl2 normalized data:\n", data_normalized_l2)

import numpy as np
from sklearn import preprocessing

input_labels = ['red', 'blасk', 'red', 'green', 'Ьlack','yellow', 'white']

encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

print("\n Label mapping:")
for i, item in enumerate(encoder.classes_):
  print(item, '-->', i)

test_labels = ['green', 'red', 'blасk']
encoded_values = encoder.transform(test_labels )
print("\nLabels =", test_labels )
print("Encoded values =", list (encoded_values ) )

encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list (decoded_list ) )