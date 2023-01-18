import pandas as pd
from pandas import DataFrame

data = {
    'ID': ['000001', '000002', '000003', '000004', '000005', '000006', '000007'],
    'name': ['黎明', '赵怡春', '张富平', '白丽', '牛玉德', '姚华', '李南'],
    'gender': [True, False, True, False, True, False, True],
    'age': [16, 20, 18, 18, 17, 18, 16],
    'height': [1.88, 1.78, 1.81, 1.86, 1.74, 1.75, 1.76]

}
frame = pd.DataFrame(data)
frame.loc[1, 'name'] = '赵春'
print(frame)
