import datetime
import os
import pandas as pd
# 库存转移
# 指定包含CSV文件的目录
csv_directory = '/Users/flash/LCP仓储/choice'
columns_to_extract2 =['Create Time', 'Business Order No.', 'Status',  'Business Doc. Type', 'Plan Quantity', 'Actual Quantity']
# 获取所有CSV文件
today = datetime.date.today()
name = str(today)+ 'jmho'
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name)) ]
print(csv_files)
# 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
dfs = []
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_directory, file) ,usecols=columns_to_extract2)
    # 去除列名中的'.'
    df.columns = [col.replace('.', '') for col in df.columns]
    # 去除数据中的'`'字符
    df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
    df['today_date'] = today
    dfs.append(df)

# 拼接所有DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 写入到XLSX文件
# combined_df.to_excel('/Users/flash/OneDrive/闪电快车/LCP/0422-3-拣货/tmp_th_combined_picked_data.xlsx', index=False)
combined_df.to_excel(os.path.join(csv_directory,'tmp_th_combined_picked_data.xlsx'), index=False)
print("所有CSV文件已拼接并写入到'combined_data.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")