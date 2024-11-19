# -*- coding: utf-8 -*-
"""Model Training.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/141ERlqvf6pWqd4XzibB-nZLwukpV8fJP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv('/content/dataFan.csv')
print(data)

X=data.iloc[:,:-1]
y=data.iloc[:,-1]
print(y)

acc_arr=[]
N=list(range(1,13,2))
for n in N:
  model=KNeighborsClassifier(n_neighbors=n)
  model.fit(X,y)
  acc_arr.append(accuracy_score(model.predict(X.values),y))
plt.plot(N,acc_arr)
plt.show()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

acc_arr=[]
N=list(range(1,13,2))
for n in N:
  model=KNeighborsClassifier(n_neighbors=n)
  model.fit(X_train,y_train)
  acc_arr.append(accuracy_score(model.predict(X_test.values),y_test))
plt.plot(N,acc_arr)
plt.show()

model=KNeighborsClassifier(n_neighbors=1)
model.fit(X,y)

#Save model as a separate file
import pickle
file= open('ml_Model','wb')
pickle.dump(model,file)
file.close()