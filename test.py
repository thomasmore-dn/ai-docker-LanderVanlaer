import json

import requests
from sklearn import datasets

digits = datasets.load_digits()

X = digits.data
y = digits.target

url = "http://localhost:80/predict"

wrong = 0
right = 0

for i in range(100):
    data = {"X": json.dumps(list(X[i]))}
    response = requests.get(url, params=data)
    y_pred = response.text

    if y[i] == int(y_pred):
        right += 1
    else:
        wrong += 1

    print("Actual:", y[i], "Predicted:", y_pred, y[i] == int(y_pred))

print()

print("Right:", right, "Wrong:", wrong)
print("Accuracy:", right / (right + wrong))
