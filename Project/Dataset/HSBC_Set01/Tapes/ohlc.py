# OHLC.py: for DSMP 2023 Project B, HSBC

# a script to accept a bunch of *tapes.csv files and output OHLC summary data

import sys
import pandas as pd


if __name__ == "__main__":

    fcount = 1
    tape_price_col = 1
    argv = sys.argv
    argc = len(argv)
    if argc > 1:
        print('Date,Open,High,Low,Close')
        while fcount < argc-1:
            # process this argument as a filename
            fname = argv[1+fcount]
            # print('fcount=%s %s' % (fcount, fname))
            extension = fname[-4:]

            if extension == '.csv':
                # good so far: now parse date from filename
                date_str = fname[10:20]
                df = pd.read_csv(fname, usecols=[tape_price_col])
                df.columns = ['price']
                length = len(df['price'])
                price_open = df['price'][1]
                price_high = df['price'].max()
                price_low = df['price'].min()
                price_close = df['price'][length-1]
                print("%s,%s,%s,%s,%s" % (date_str, price_open, price_high, price_low, price_close))
                df = df.iloc[0:0]   # erase this df
            else:
                print('FAIL: file with extension=%s can\'t be handled' % extension)
                sys.exit(0)

            fcount += 1
