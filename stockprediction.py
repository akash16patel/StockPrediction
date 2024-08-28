from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import requests
import json
import urllib.request,json
import os
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler






if __name__=="__main__":
    data_source='alphavantage'
    if data_source=='alphavantage':
        api_key='H2AG8Z6YLB051TF6'
        ticker=input("Which stock prediction you want please write their symbol:")
        url_string = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&outputsize=full&apikey={api_key}"
        file_to_save=f'stock_market_data-{ticker}.csv'

        if not os.path.exists(file_to_save):
            # with urllib.request.urlopen(url_string) as url:
                #data=json.loads(url.read().decode())
            response=requests.get(url_string)
                #extract stock market data
                # data=data['Time Series (Daily)']
            data=response.json()
            df=pd.DataFrame(columns=['Date','Low','High','Close','Open'])
            for k,v in data.items():
                    date=dt.datetime.strptime(k,'%Y-%m-%d')
                    data_row=[date.date(),float(v['3. low']),float(v['2. high']),float(v['4. close']),float(v['1. open'])]
                    df.loc[-1,:]=data_row
                    df.index=df.index+1
            print('Data saved to :%s'%file_to_save)
            df.to_csv(file_to_save)
        else:
            print(f'File already exists. loading data from csv')
            df=pd.read_csv(file_to_save)
    else:
        df=pd.read_csv(os.path.join('Stocks','hpq.us.txt'),delimiter=',',usecols=['Date','Open','High','Close','Low'])
        print('Loaded data from the kaggle repository')

