import pandas as pd
import os

# 读取CSV文件
csv_file = '/Users/flash/OneDrive/闪电快车/LCP/0404经营分析日报/202403订单详情/202403账单详细数据.csv'
df = pd.read_csv(csv_file)

# 获取CSV文件的行数
num_rows = df.shape[0]

# 定义每个工作表的最大行数（根据Excel的限制，这里假设为100万行）
max_rows_per_sheet = 1000000

# 计算需要多少个工作表
num_sheets = num_rows // max_rows_per_sheet + (1 if num_rows % max_rows_per_sheet != 0 else 0)

# 创建一个Excel writer对象
excel_writer = pd.ExcelWriter('/Users/flash/OneDrive/闪电快车/LCP/0404经营分析日报/202403订单详情/202403账单详细数据split_file.xlsx', engine='openpyxl')

# 将数据分块并写入到不同的工作表中
for i in range(num_sheets):
    # 计算每个工作表的起始和结束行
    start_row = i * max_rows_per_sheet
    end_row = (i + 1) * max_rows_per_sheet if (i + 1) * max_rows_per_sheet < num_rows else num_rows
    # 分割数据
    df_sheet = df[start_row:end_row]
    # 将数据写入到工作表
    df_sheet.to_excel(excel_writer, sheet_name=f'Sheet{i+1}', index=False, startrow=0, header=True)

# 保存Excel文件
excel_writer.save()
