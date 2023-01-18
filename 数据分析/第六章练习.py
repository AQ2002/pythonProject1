import pandas as pd
import matplotlib.pyplot as plt

records = pd.read_csv('lending.dat')
records['year'] = pd.to_datetime(records['date']).dt.year
results = records[['uid', 'year']].groupby('year').count()
plt.plot(results['uid'])
# plt.scatter(results.index, results['uid'])
# plt.bar(results.index, results['uid'])
plt.show()
