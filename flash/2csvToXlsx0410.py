import pandas as pd
# 未上架
path='/Users/flash/OneDrive/闪电快车/LCP/0404经营分析日报/202403订单详情/202403账单详细数据.csv'
# columns_to_extract2 =['Create Time', 'Task Id', 'Manufacturer barcode',  'Container Code', 'Plan Quantity']
# 读取CSV文件
df = pd.read_csv(path, error_bad_lines=False )

# 将DataFrame写出到XLSX文件
df.to_excel('/Users/flash/OneDrive/闪电快车/LCP/0404经营分析日报/202403订单详情/202403账单详细数据.xlsx', index=False)

print('CSV文件已转换为XLSX文件。需要手动删字段')