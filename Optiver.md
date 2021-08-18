# Optiver Realized Volatility Predictionコンペの概要

___

- Volatility(ボラティリティー)とは
 - オプション取引
 - 取引の価格変動のこと

**商品のリスクの大きさの目安として使用**

___

このコンペでは、最初の３ヶ月間でモデルを作成し  
最終結果は、３ヶ月間の評価を得て決まる

___

## 用語説明

### bitとask

- bit  
売り(証券を売る際のprice)
- ask  
買い(証券を買う際のprice)
- spread(スプレッド)  
bitとaskの差  
取引が激しくなるor極端に低下するとスプレッドが広がる


[ex.](https://www.youtube.com/watch?v=dHyPrG9vM3w)  
bid(売り)102.10  
ask(買い)102.15  
この時に買ってすぐ売ると0.05円分手数料（評価損益）として取られる  
この手数料がspread



### Weighted averaged price(WAP)

- VWAP
 - 出来高加重平均価格
 - 今日売買した人の純粋な平均価格


### Log returns

株価の変化率


### Realized volatility

通常は1年の期間に正規化され、年換算の標準偏差はボラティリティと呼ばれる


___

## データの説明

- book_[train/test].parquet  
市場に投入された最も競争力のある売買注文に関するオーダーブックデータ

- trade_[train/test].parquet  
実際に実行された取引に関するデータ

