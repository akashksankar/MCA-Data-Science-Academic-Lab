import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
data = pd.read_csv('diabetes.csv')
print(data.head())
x = data.iloc[:, 1]
print(x.head())
y = data.iloc[:, 6]
print(y.head())
x = np.array(x).reshape(-1, 1)
print(x)
print()
y = np.array(y).reshape(-1, 1)
print(y)
print()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
classifier = LinearRegression()
classifier.fit(x_train, y_train)
print(classifier)
y_pred = classifier.predict(x_test)
print(y_pred)
print()
print("R-squared score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Coefficients:", classifier.coef_)
plt.scatter(x_test, y_test, color='b', label='Actual')
plt.plot(x_test, y_pred, color='k', label='Predicted')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Linear Regression Results')
plt.legend()
plt.show()


from sklearn import linear_model
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
irisData = load_iris()
X = irisData.data
Y = irisData.target
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=7, random_state=42)
model = linear_model.LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
y_pred_train = model.predict(x_train)
print("Mean square error =", mean_squared_error(y_test, y_pred))
print("R2 Score =", r2_score(y_test, y_pred))