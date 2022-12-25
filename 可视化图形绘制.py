import pandas as pd
import matplotlib.pyplot as plt
frame1=pd.read_csv('股票数据.csv',encoding='GBK')
frame1=frame1.set_index('日期')
frame1.index=pd.to_datetime(frame1.index)

frame2=pd.read_csv('股票数据.csv',encoding='GBK')
frame2=frame2.set_index('换手率')
frame2.index=pd.to_datetime(frame2.index)

plt.plot(frame1['最低价'])
plt.plot(frame2['最高价'])
plt.show()