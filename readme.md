# Kaggle日記
## Optiver Realized Volatility Prediction

___

### 2021/08/09
- リポジトリ作成


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

### 2021/08/15
- 新たな特徴量の作成,lgbm  
[参考にしたNotebook](https://www.kaggle.com/tommy1028/lightgbm-starter-with-feature-engineering-idea)
- logreturn  
time_idでguroupbyしてpriceまたはwapのlog.diffを返したもの  
なのでtime_idの種類分Naがある

### 2021/08/16
- 先日のNotebookを引き続き進めた。  
残るはlgbmのモデルづくり

### 2021/08/17
- お休み

### 2021/08/18
- 一昨日のNotebookを引き続き進めた。  
とりあえずlgbmのNotebookは終了した  
これ以上どのように特徴量をいじればいいのかわからない...
- いったん整理するために[Optiver取り組む前準備・用語の説明](https://www.kaggle.com/takiyu/japanese-optiver)このNotebookを読んでOptiver.mdにまとめた


### 2021/08/19 ~ 
- 競技プログラミングと数学の勉強に集中したいのでしばらくお休み...
