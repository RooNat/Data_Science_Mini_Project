Problem B: HSBC Data Sets

Each data-set covers roughly six months of trading, one file per day, 
with the filename showing the relevant date. Each data-set is in a folder 
that contains two sub-folders: LOBs and Tapes. 

The files in LOBs are the daily records of Limit Order Book data for the 
one asset that we have recorded data for: each row of this file is the 
timestamp, the exchange-I.D. (which is always "Exch0" because we've only 
recorded data for a single exchange) and then the bid and ask sides of 
the LOB. Every time the LOB changes, a new row is printed to the LOB 
file.

The files in Tapes are the daily transaction data (from the Exchange's 
"tape", its record of activity): each row is time, price, and quantity 
for a single transaction in the one asset we have recorded trading data 
for. There are typically more than 25000 transactions per day.  

A common way of summarising high volumes of trading data over some period 
is to record only the opening price at the start of the period, the 
closing price at the end of the period, and the highest and lowest prices 
recorded within the period: this is known as OHLC data, and is often 
plotted on a "candlestick" chart. In the Tapes folder you will find a 
simple Python script called ohlc.py which if you run as:

Python3 ohlc.py *tapes.csv > ohlc.csv

Will give you a csv file of the OHLC data, and from that you can plot a 
chart as in the Excel spreadsheet ohlc.xlsx, also supplied in the Tapes 
folder. 

In both LOBs and Tapes, timestamps are seconds since market opened on 
that day.

Note that traders can cancel their orders on the LOB, so some changes in 
the LOB are not reflected in the corresponding tape data: that is, 
sometimes the LOB changes due to cancellations rather than due to 
transactions. 



