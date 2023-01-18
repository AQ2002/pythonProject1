# 打印出一个表
import pandas as pd
from pandas import DataFrame

# DataFrame是一个表格型的数据结构

data = {'ID': ['000001', '000002', '000003', '000004', '000005', '000006', '000007'],
        'name': ['黎明', '赵怡春', '张富平', '白丽', '牛玉德', '姚华', '李南'],
        'gender': [True, False, True, False, True, False, True],
        'age': [16, 20, 18, 18, 17, 18, 16],
        'height': [1.88, 1.78, 1.81, 1.86, 1.74, 1.75, 1.76]
        }
frame = pd.DataFrame(data)
print(frame['name'])  # ①print(frame.name)等效
print(frame[2:4])  # 通过行的序显示，[a:b]通常包含a但不包含b
print(frame[2:7:2])  # 表示从2到7中每两个显示一行
print(frame[2:3]['name'])  # 行和列的前后位置都不影响
print(frame.loc[3])  # 显示序号为3的一整行
print(frame.loc[1:4])  # 序号1到4，loc[a:b]包含a和b
print(frame.loc[[1, 3]])  # 选择不连续的行
print(frame.loc[:, ['name', 'age', 'height']])  # 用：表示所有行
print(frame.iloc[2, 4])  # 精准输出行和列对应的，因为从0开始的所以实际输出是3行5列
print(frame.iloc[1:3, 2:4])  # iloc函数也不包含[a,b]中的b，实际上只有loc函数才包含

