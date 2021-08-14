from sklearn.model_selection import KFold
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import StandardScaler


def set_data():
    global test
    test = pd.read_csv(r'input\test.csv')
    train = pd.read_csv(r'input\train.csv')

    train["row_id"] = train["stock_id"].astype(str)+"-"+train["time_id"].astype(str)

    stock = train.groupby("stock_id")['target'].agg(["mean","median","std","count","sum"]).reset_index()
    time = train.groupby(["time_id"])["target"].agg(["mean","median","std","count","sum"]).reset_index()
    row = train.groupby(["row_id"])["target"].agg(["mean","median","std","count","sum"]).reset_index()

    train_info = train.copy()
    train_info['stock_id_mean']     = train['stock_id'].map(dict(zip(stock['stock_id'], stock['mean'])))
    train_info['stock_id_median']   = train['stock_id'].map(dict(zip(stock['stock_id'], stock['median'])))
    train_info['stock_id_std']      = train['stock_id'].map(dict(zip(stock['stock_id'], stock['std'])))
    train_info['time_id_mean']      = train['time_id'].map(dict(zip(time['time_id'], time['mean'])))
    train_info['time_id_median']    = train['time_id'].map(dict(zip(time['time_id'], time['median'])))
    train_info['time_id_std']        = train['time_id'].map(dict(zip(time['time_id'], time['std'])))
    train_info['row_id_mean']      = train['row_id'].map(dict(zip(row['row_id'], row['mean'])))
    train_info['row_id_median']    = train['row_id'].map(dict(zip(row['row_id'], row['median'])))
    train_info['row_id_std']        = train['row_id'].map(dict(zip(row['row_id'], row['std'])))
    
    y = train_info["target"]
    X = train_info.drop(["stock_id","time_id","target","row_id"],axis=1)

    test_info = test.copy()
    test_info['stock_id_mean']     = test['stock_id'].map(dict(zip(stock['stock_id'], stock['mean'])))
    test_info['stock_id_median']   = test['stock_id'].map(dict(zip(stock['stock_id'], stock['median'])))
    test_info['stock_id_std']      = test['stock_id'].map(dict(zip(stock['stock_id'], stock['std'])))
    test_info['time_id_mean']      = test['time_id'].map(dict(zip(time['time_id'], time['mean'])))
    test_info['time_id_median']    = test['time_id'].map(dict(zip(time['time_id'], time['median'])))
    test_info['time_id_std']       = test['time_id'].map(dict(zip(time['time_id'], time['std'])))
    test_info['row_id_mean']      = test['row_id'].map(dict(zip(row['row_id'], row['mean'])))
    test_info['row_id_median']    = test['row_id'].map(dict(zip(row['row_id'], row['median'])))
    test_info['row_id_std']        = test['row_id'].map(dict(zip(row['row_id'], row['std'])))

    X_test = test_info.drop(["stock_id","time_id","row_id"],axis=1)

    return X,y,X_test

def rmspe(y_true,y_pred):
    yt = np.array(y_true)
    yp = np.array(y_pred)
    res = np.square((yt-yp)/yp)
    res = np.sqrt(np.mean(res))
    return res


def run():
    X,y,X_test = set_data()

    kf = KFold(n_splits=5,random_state=123,shuffle=True)

    scaler = StandardScaler()
    scaler.fit(X)
    scores = []

    model = xgb.XGBRegressor()

    for train_index, val_index in kf.split(X, y):
        X_train = scaler.transform(X.iloc[train_index,:])
        y_train = y[train_index]
        X_val  = scaler.transform(X.iloc[val_index,:])
        y_val  = y[val_index]

        model.fit(X_train,y_train)
        y_pred = model.predict(X_val)

        # plt.plot(y_pred,y_val,'x')
        scores.append((rmspe(y_val,y_pred)))
    
    print(f"average score = {sum(scores)/len(scores)}")
    
    model.fit(scaler.transform(X),y)
    y_pred = model.predict(scaler.transform(X_test))

    return y_pred


if __name__=="__main__":
    y_pred = run()
    sub = test.copy()
    sub["target"] = y_pred
    sub.drop(["stock_id","time_id"],axis=1,inplace=True)
    print(sub)
    # sub.to_csv("submission.csv", index=False)
    