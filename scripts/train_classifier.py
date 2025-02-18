import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('data/data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, shuffle=True, stratify=labels, random_state=42)

model = RandomForestClassifier(random_state=42)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_test, y_predict)

print('{}% of samples were classified correctly!'.format(round(score * 100, 2)))

with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)