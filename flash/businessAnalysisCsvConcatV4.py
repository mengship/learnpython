
import pandas as pd
import os

# 设置工作目录到包含CSV文件的目录
os.chdir('/Users/flash/LCP仓储/经营分析日报4月/包裹详情-计算包材/0301')

# 初始化一个空的DataFrame来存储拼接后的数据
concatenated_df = pd.DataFrame()

# 遍历目录下的所有CSV文件
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        # 读取CSV文件
        df = pd.read_csv(filename)

        # 选择特定的列
        selected_columns = df[['Package No.', 'Recommended Packaging Material Code', 'Packaging Material Code', 'Goods Issue Time']]  # 替换为你的列名

        # 将文件名作为新的一列添加到DataFrame中，以便追踪数据来源
        # selected_columns.loc['Filename'] = filename

        # 将选择的列追加到concatenated_df中
        concatenated_df = pd.concat([concatenated_df, selected_columns], ignore_index=True)

# 将拼接后的数据写入新的Excel文件
concatenated_df.to_excel('concatenated_data0301.xlsx', index=False)

print('数据已拼接并写入新的Excel文件。')
