import numpy as np
import pandas as pd
import joblib

# model load
classification = joblib.load('./Models/logistic.pkl')
bukhan = joblib.load('./Models/bukhan.pkl')
chiak = joblib.load('./Models/chiak.pkl')
gyeryong = joblib.load('./Models/gyeryong.pkl')
jiri = joblib.load('./Models/jiri.pkl')
naejang = joblib.load('./Models/naejang.pkl')

# 분류 레이블에 따른 각각의 예측 모델
prediction = {1:bukhan, 2:chiak, 3:gyeryong, 4:jiri, 5:naejang}

data = pd.read_csv('./data/2023_mt.csv')

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
input = data.iloc[:, :6]    # original
input2 = scaler.fit_transform(input)   # for classification
real = data.iloc[:, -1]

result = np.zeros((1, input.shape[0]))
for i in range(input.shape[0]):
    test = input2[i].reshape(1, input.shape[1])  # for classification
    test2 = input.iloc[i, :].to_numpy().reshape(1, input.shape[1])  # for prediction
    label = classification.predict(test)
    pred = prediction[label[0]].predict(test2)
    result[0][i] = round(pred[0])

    print(result)

'''
input = data.iloc[:, :6]
elv = data.iloc[:, -2]  # 분류를 위한 지리적 정보
real = data.iloc[:, -1]

# 높이를 이용한 산 분류
result = np.zeros((1, input.shape[0]))
for i in range(input.shape[0]):
    test = input.iloc[i, :].to_numpy().reshape(1, input.shape[1])
    if elv[i] == 835.6:
        label = 1
    elif elv[i] == 1282.0:
        label = 2
    elif elv[i] == 402.5:
        label = 3
    elif elv[i] == 1915.4:
        label = 4
    elif elv[i] == 763.5:
        label = 5
    pred = prediction[label].predict(test)
    result[0][i] = round(pred[0])

    print(result)
'''