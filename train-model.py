import pickle

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

X = digits.data
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

reg = LogisticRegression(max_iter=2000)
reg.fit(X_train, y_train)

print(reg.score(X_test, y_test))

pickle.dump(reg, open('./exports/model.pkl', 'wb'))
