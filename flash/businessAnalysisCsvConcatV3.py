import pandas as pd
import os
# 自己下载的订单详情合并
# 设置工作目录到包含CSV文件的文件夹
os.chdir('/Users/flash/OneDrive/闪电快车/LCP/0404经营分析日报/202403订单详情')

# 获取所有CSV文件的列表
csv_files = [file for file in os.listdir() if file.endswith('.csv')]

# 初始化一个空的DataFrame来存储合并后的数据
merged_data = pd.DataFrame()

# 遍历所有CSV文件并将它们合并到merged_data DataFrame中
for file in csv_files:
    data = pd.read_csv(file)
    merged_data = merged_data.append(data, ignore_index=True)

# 将合并后的数据写入新的CSV文件
merged_data.to_csv('2024-03-order.csv', index=False)
