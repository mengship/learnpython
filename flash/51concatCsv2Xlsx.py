import pandas as pd
# 未上架
path='/Users/flash/OneDrive/闪电快车/LCP/0404-5-判责/tmp_th_20240327_Fail_Task_Recheck.xlsx'
# 读取CSV文件
df = pd.read_excel(path, error_bad_lines=False)
# 将假设你要替换列名中的所有'.'字符为' '
df.columns = df.columns.str.replace('.', '')
# 遍历所有列，如果是字符串类型，则替换掉反引号
for column in df.columns:
    # 去除数据中的'`'字符
    df = df.applymap(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
# 将DataFrame写出到XLSX文件
df.to_excel('/Users/flash/OneDrive/闪电快车/LCP/0404-5-判责/tmp_th_20240327_Fail_Task_Recheckv1.xlsx', index=False)

print('CSV文件已转换为XLSX文件。需要手动删字段')