from utils.data_io import load_train, load_test
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

train_data = load_train()

x = train_data.drop('y', axis=1)
y = train_data.y

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=31415)

enc = OneHotEncoder()
clf = LinearRegression(fit_intercept=True)
