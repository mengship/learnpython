import glob
import datetime
import os
import pandas as pd
# 上架
# 指定包含CSV文件的目录
csv_directory = '/Users/flash/LCP仓储/choice'
columns_to_extract2 =['Create Time', 'Task Id', 'Manufacturer barcode',  'Container Code', 'Plan Quantity']
today = datetime.date.today()
name = str(today)+ 'uhjw'
# 获取所有CSV文件
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name)) ]

# 获取文件夹中所有.txt文件的路径
# 将excel中的 \, 替换掉
# file_paths = glob.glob(os.path.join(csv_directory, '*.csv'))
file_paths = [os.path.join(csv_directory, file) for file in csv_files]
print(file_paths)

# 遍历所有文件
for file_path in file_paths:
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 过滤掉 "\," 特殊字符
    filtered_content = content.replace('\\,', '')

    # 将过滤后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(filtered_content)

print("将excel中的 \, 替换掉，所有文件处理完成。")



# 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
dfs = []
print(csv_files)
for file in csv_files:
    df = pd.read_csv(os.path.join(csv_directory, file) ,usecols=columns_to_extract2)
    # 去除列名中的'.'
    df.columns = [col.replace('.', '') for col in df.columns]
    # 去除数据中的'`'字符
    df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
    dfs.append(df)

# 拼接所有DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 写入到XLSX文件
# combined_df.to_excel('/Users/flash/OneDrive/闪电快车/LCP/0422-2-上架/tmp_th_NotCompletedShelves.xlsx', index=False)
combined_df.to_excel(os.path.join(csv_directory, 'tmp_th_NotCompletedShelves.xlsx'), index=False)

print("所有CSV文件已拼接并写入到'combined_data.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")