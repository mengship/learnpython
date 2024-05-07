from datetime import datetime
import os
import pandas as pd
# 库存转移
# 指定包含CSV文件的目录
csv_directory = '/Users/flash/OneDrive/闪电快车/LCP/0419-3-拣货'
columns_to_extract2 =['Create Time', 'Business Order No.', 'Status',  'Business Doc. Type', 'Plan Quantity', 'Actual Quantity']
# 获取所有CSV文件
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
dfs = []
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_directory, file) ,usecols=columns_to_extract2)
    # 去除列名中的'.'
    df.columns = [col.replace('.', '') for col in df.columns]
    # 去除数据中的'`'字符
    df = df.applymap(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
    # 增加当日日期列
    today = datetime.now().strftime('%Y-%m-%d')
    df['today_date'] = today
    dfs.append(df)

# 拼接所有DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 写入到XLSX文件
combined_df.to_excel('/Users/flash/OneDrive/闪电快车/LCP/0419-3-拣货/tmp_th_combined_picked_data.xlsx', index=False)

print("所有CSV文件已拼接并写入到'combined_data.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")