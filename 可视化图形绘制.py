import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
frame=pd.read_csv('股票数据.csv',encoding='GBK')
frame=frame.set_index('日期')
frame.index=pd.to_datetime(frame.index)

plt.scatter(frame['开盘价'],frame['收盘价'],c=frame['成交量'],s=frame['换手率'],alpha=0.5)
plt.colorbar()
plt.show()