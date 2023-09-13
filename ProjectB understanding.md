# Problem B

In the trade market, there are so many people buying and selling assets that the share price can potentially move up and down several times per second

Hence in one trading-day there could be 20,000 or more time-points for movements in the price of an asset.



This would be quite a lot to process if the data of interest at each time-point was only a single value



Traders in financial markets commonly work with data that summarises all **bids** (orders to buy) and **asks** (orders to sell) currently resting at the exchange: 

1. any trader looking to buy can post a "**bid limit order**" at the exchange, saying what price they are prepared to pay per share, and how many shares they wish to buy; 
2. similarly, any seller can post an "**ask limit order**" showing how many shares they want to sell, and the per-share price they are seeking.
3. Different buyers will have different price and quantity needs, as will different sellers, and so at any one time the stock-exchange summarises all of the currently-received orders by publishing its **"Limit Order Book" (LOB)**, sometimes also called the ladder, which shows the total quantity of units of the asset available to buy or to sell at each price which has been quoted.



The LOB at any one time will typically involve tens of different (price, quantity) pairs – and the LOB may change several times before any transaction takes place that results in a change in the share-price



