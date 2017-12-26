import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
boston = load_boston()
# print(boston.keys())
# print(boston.data.shape)
# print(boston.target.shape)
# print(boston.feature_names)
# print(boston.DESCR)


df = pd.DataFrame(boston.data, columns=boston.feature_names)
# print(df)
df['PRICE'] = boston.target
# print(df.head)
# print(boston)
# USAHousing = pd.read_csv("USA_Housing.csv")

# print(USAHousing.head())
# print(USAHousing.describe())
# print(USAHousing['Address'][0])
# sns.pairplot(USAHousing)

X = boston.data
y = boston.target

X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size=0.33, random_state=42)
lm = LinearRegression()
lm.fit(X_train, y_train)


predict_y = lm.predict(X_test);
# print(predict_y)

residuals = pd.Series((y_test - predict_y)/20)

# los = y_test - predict_y

print(residuals)
residuals.hist(bins=50)

import seaborn as sns

sns.set()
df = sns.load_dataset('iris')
sns.pairplot(df, hue='species', size=2.5)
plot.show()
