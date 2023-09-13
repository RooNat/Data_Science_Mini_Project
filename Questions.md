# Questions/Todo

Documents: https://docs.google.com/document/d/1eauvQy0ecLLA8gZolYDsIbLAksGehiUN2_FbBEZYXr4/edit?usp=sharing

- [x] When should we start to submit the activity log? from week 3

- [ ] What does the LOB look like?

- [ ] What method should we use to predict?

- [x] What is the LOB[(Limit order books](https://www.investopedia.com/terms/l/limitorderbook.asp#:~:text=Key%20Takeaways-,A%20limit%20order%20book%20is%20a%20record%20of%20outstanding%20limit,record%20by%20the%20security%20specialist.))

  https://zhuanlan.zhihu.com/p/386762738

- [ ] A3C system

- [ ] ARIMA1

- [ ] Mid-Price prediction

  - [ ] **learn about LSTM** time series
  - [ ] learn about CNN time series
  - [ ] Download the relevant code
  - [ ] Run the code

- [ ] ARIMA optimise

- [ ] Plot 

- [ ] Simulator



1. **What would cause the share price rise or fall?**

   https://trading.info/stock-rise-fall/

   https://www.investopedia.com/articles/basics/04/100804.asp

2. **Order book**

​		https://learn.bybit.com/trading/order-book-explained-for-beginners/

​		https://stanford.edu/~ashlearn/RLForFinanceBook/chapter9.pdf

​		https://www.mdpi.com/2227-7390/10/8/1234

3. **Reinforcement learning**

   https://www.analyticsvidhya.com/blog/2020/10/reinforcement-learning-stock-price-prediction/



4. Time series

   https://medium.com/lemon-markets/using-time-series-forecasting-to-predict-stock-prices-b1346ef0cc5a

### Week3

- [ ] Use AWS to process data
- [ ] Build a database with mysql and import the csv file into database



### Week4

- [x] Process all data--- Data Preprocessing



### Week5

- [ ] ARIMA model data process

- [x] https://www.youtube.com/watch?v=g6WZyHwd7oY

- [ ] PCA ?

- [ ] https://lobsterdata.com/info/DataStructure.php

- [ ] https://www.kaggle.com/datasets/martinsn/high-frequency-crypto-limit-order-book-data

- [ ] Relevant concepts about the limit order book

- [ ] https://www.kaggle.com/code/saurabhshahane/stock-prices-predictions-eda-lstm-deepexploration

- [ ] https://www.kaggle.com/code/praanj/limit-orderbook-visualizer-plotly

- [ ] How to understand the OHLC, 

- [ ] https://www.kaggle.com/code/nageshsingh/stock-market-forecasting-arima

- [ ] Relevant limit order papers

- [ ] https://www.projectpro.io/article/how-to-build-arima-model-in-python/544

- [ ] https://www.analyticsvidhya.com/blog/2021/07/stock-market-forecasting-using-time-series-analysis-with-arima-model/

  

### LSTM

https://www.simplilearn.com/tutorials/machine-learning-tutorial/stock-price-prediction-using-machine-learning



## Reading list

There is a vast literature out there which is potentially relevant to this project. The readings listed here are likely to be helpful, but there are many others that could be just as useful.

Abergel, F., Anane, M., Chakrabort, A., Jedidi, A., and Toke, I. (2016) Limit Order Books, Cambridge University Press

Bouchaud, J., Bonart, J., Donier, J., and Gould, M. (2018), Trades, Quotes, and Prices: Financial Markets Under the Microscope. Cambridge University Press.

Gould, M., Porter., M. Williams, S., McDonald, M., Fenn, D., and Howison, S. (2013) Limit Order Books. Quantitative Finance, 13(11):1709-1742. Available from: https://people.maths.ox.ac.uk/porterm/papers/gould-qf-final.pdf



### References

A common way of summarising **high volumes** of trading data over some period is to record only the **opening price at the start of the period**, **the closing price at the end of the period**, **and the highest and lowest prices recorded within the period**: this is known as OHLC data, and is often plotted on a "candlestick" chart. In the Tapes folder you will find a simple Python script called ohlc.py which if you run as:

```python
Python3 ohlc.py *tapes.csv > ohlc.csv
```

Will give you a csv file of the OHLC data, and from that you can plot a chart as in the Excel spreadsheet ohlc.xlsx, also supplied in the Tapes folder. 

