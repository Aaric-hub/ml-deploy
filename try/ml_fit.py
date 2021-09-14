# doing necessary imports...
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, Lasso, RidgeCV, LassoCV, ElasticNet, ElasticNetCV, LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle


def instance_fit():
    try:
        df_actual = pd.read_csv("Test_case.csv")
        y = df_actual["Machine failure"]
        x = df_actual[["TWF", "HDF", "PWF", "OSF"]]
        scaler = StandardScaler()
        arr = scaler.fit_transform(x)
        x_train, x_test, y_train, y_test = train_test_split(arr, y, test_size=0.25, random_state=350)
        lr = LinearRegression()
        lr.fit(x_train, y_train)

        file = "linear_reg.sav"
        pickle.dump(lr, open(file, 'wb'))

    except Exception as e:
        raise Exception(f"(instance_fit): Something went wrong: "+str(e))