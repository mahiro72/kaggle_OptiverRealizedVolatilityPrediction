from sklearn.model_selection import KFold
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import StandardScaler


def read_data():
    global train,test
    test = pd.read_csv(r'input\test.csv')
    train = pd.read_csv(r'input\train.csv')


def run():
    stock = train.groupby("stock_id")['target'].agg(["mean","median","std","count","sum"]).reset_index()
    time = train.groupby(["time_id"])["target"].agg(["mean","median","std","count","sum"]).reset_index()

    train_info = train.copy()
    train_info['stock_id_mean']     = train['stock_id'].map(dict(zip(stock['stock_id'], stock['mean'])))
    train_info['stock_id_median']   = train['stock_id'].map(dict(zip(stock['stock_id'], stock['median'])))
    train_info['stock_id_std']      = train['stock_id'].map(dict(zip(stock['stock_id'], stock['std'])))
    train_info['time_id_mean']      = train['time_id'].map(dict(zip(time['time_id'], time['mean'])))
    train_info['time_id_median']    = train['time_id'].map(dict(zip(time['time_id'], time['median'])))
    train_info['time_id_std']        = train['time_id'].map(dict(zip(time['time_id'], time['std'])))

    kf = KFold(n_splits=5,random_state=123,shuffle=True)

    y = train_info["target"]
    X = train_info.drop(["stock_id","time_id","target"],axis=1)

    scaler = StandardScaler()
    scaler.fit(X)


    test_info = test.copy()
    test_info['stock_id_mean']     = test['stock_id'].map(dict(zip(stock['stock_id'], stock['mean'])))
    test_info['stock_id_median']   = test['stock_id'].map(dict(zip(stock['stock_id'], stock['median'])))
    test_info['stock_id_std']      = test['stock_id'].map(dict(zip(stock['stock_id'], stock['std'])))
    test_info['time_id_mean']      = test['time_id'].map(dict(zip(time['time_id'], time['mean'])))
    test_info['time_id_median']    = test['time_id'].map(dict(zip(time['time_id'], time['median'])))
    test_info['time_id_std']       = test['time_id'].map(dict(zip(time['time_id'], time['std'])))



    model = xgb.XGBRegressor()
    X_test = test_info.drop(["stock_id","time_id","row_id"],axis=1)
    model.fit(scaler.transform(X),y)
    y_pred = model.predict(scaler.transform(X_test))

    return y_pred


if __name__=="__main__":
    read_data()
    y_pred = run()
    sub = test.copy()
    sub["target"] = y_pred
    sub.drop(["stock_id","time_id"],axis=1,inplace=True)
    print(sub)
    # sub.to_csv("submission.csv", index=False)