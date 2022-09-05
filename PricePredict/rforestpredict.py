import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



data = pd.read_csv("G:\\4hourdata.csv",sep=",")
data.rename(columns={"Open":"Open","High":"High","Low":"Low","Close":"Close"},inplace=True)
lis1=data["Open"]
lis2=data["High"]
lis3=data["Low"]
lis4=data["Close"]

df = pd.DataFrame(list(zip(lis1,lis2,lis3,lis4)),
               columns =['Open','High','Low','Close'])


X=np.array(data["OpenTime"])
Y=np.array(df)

scaler = StandardScaler()

X=scaler.f
(X.reshape(-1,1))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
X_train.reshape(-1,1)
X_test.reshape(-1,1)
regressor = RandomForestRegressor(n_estimators = 10, random_state = 42)
regressor.fit(X_train, Y_train)