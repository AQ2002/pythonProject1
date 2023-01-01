import pandas as pd
records = pd.read_csv('lending.dat')

# ①查询人间词话借阅情况
print(records[records['title'] == '人间词话'])
print(records.loc[records['title'] == '人间词话'])
print(records[records['title'] == '人间词话']['uid'])
print(records[records['title'] == '人间词话'][['uid', 'date']])

# ②查阅2016年的借阅情况
records['newDate'] = pd.to_datetime(records['date'])
print(records[records['newDate'].dt.year == 2016])
