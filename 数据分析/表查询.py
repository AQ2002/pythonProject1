import pandas as pd
frame=pd.read_csv('股票数据.csv', encoding='GBK')

#print(frame[(frame['最高价'] == frame['最低价']) & (frame['最高价'] != 0)])
#print(frame[(frame['收盘价']>frame['前收盘'])])
#print(frame[(frame['成交笔数']>30000)|((frame['换手率']<0.2)&frame['收盘价']!=0)])
print(frame[(pd.to_datetime(frame['日期']).dt.year == 2019) &
            (pd.to_datetime(frame['日期']).dt.month == 12)])