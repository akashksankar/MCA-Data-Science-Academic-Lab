from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pandas as pd

from exp30 import y_pred

data=pd.read_csv('Iris.csv')
print(data.head())
print()
x=data.iloc[:,:-4]
y=data.iloc[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20)
classifier=SVC(kernel='linear')
classifier.fit(x_train,y_train)
print(classifier)
print()
y_pred=classifier.predict(x_test)
print("array",y_pred)
print()
cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix:\n",cm)
print()
ac=accuracy_score(y_test,y_pred)
print("Accuracy Score:",ac)