# Kaggle日記
## Optiver Realized Volatility Prediction

___

### 2021/08/09
- リポジトリ作成

___

### 2021/08/10
- edaとコンペの概要把握  
[参考にしたNotebook](https://www.kaggle.com/chumajin/optiver-realized-eda-for-starter-version)  
- 中央値でうめてお試しsubmit

### 2021/08/11
- 金融の基礎知識など
[参考にしたNotebook](https://www.kaggle.com/jiashenliu/introduction-to-financial-concepts-and-data)  
- [eda2](https://www.kaggle.com/matsuosan/optiver-eda-xgboost-starter-japanese#realized_volatility) データについてより詳細に確認
- wap,log_return,realized_volatilityが重要
- targetは歪度がおそらく高いので対数をとる必要がありそう？

### 2021/08/12
- 前日に引き続き同じnotebookをみながらeda  
あまり進展なし

### 2021/08/13
- 前日に引き続き同じeda  
LinearRegressionのモデルで分析  
score = 0.98

### 2021/08/14
- 最初のxgboostモデル作成
- mean median std を stock_idで分けたものと  
time_idで分けたものの6列を特徴量とした  
kfoldで交差検証したところscoreは0.26だった  
public scoreは0.52071
- xgboost model var.2  
row_id　の mean median std を特徴量に追加した  
scoreは0.82 ....  
過学習しているのか?原因ははっきりわからない  
ハイパーパラメータのチューニングが必要かも  