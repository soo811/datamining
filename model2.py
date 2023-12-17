import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/total.csv')
data2 = pd.read_csv('./data/2023_mt.csv')

train_x = data.iloc[:, 1:10]
train_y = data.iloc[:, -1]
test_x = data2.iloc[:, :-1]
test_y = data2.iloc[:, -1]

# 선형회귀
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(train_x, train_y)
pred = model.predict(test_x)
print(np.around(pred))

print(model.coef_)
print(model.intercept_)