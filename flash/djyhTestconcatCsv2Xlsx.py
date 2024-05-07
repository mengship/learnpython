import datetime

import pandas as pd
# choice货主货位数据
today = datetime.date.today()
path = '/Users/flash/LCP仓储/choice/'+str(today)+'kuwzkucpuhpn.csv'
print(path)
# 读取CSV文件
df = pd.read_csv(path)
# 将假设你要替换列名中的所有'.'字符为' '
df.columns = df.columns.str.replace('.', '')
# 遍历所有列，如果是字符串类型，则替换掉反引号
for column in df.columns:
    if df[column].dtype == object:  # 只有在列是字符串类型时才进行替换
        df[column] = df[column].str.replace('`', '')
# 将DataFrame写出到XLSX文件
df.to_excel('/Users/flash/LCP仓储/choice/tmp_th_kuwzkucpuhpn.xlsx', index=False)

print('CSV文件已转换为XLSX文件。')