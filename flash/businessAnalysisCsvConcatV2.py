import pandas as pd
import os
import datetime

# 自己下载的包裹详情合并
# 设置工作目录到包含CSV文件的文件夹
os.chdir('/Users/flash/LCP仓储/经营分析日报4月/包裹详情')
startDay='2024-04-28'
today = datetime.date.today()
endDay='2024-04-30'
# todayadd45 = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
while startDay <= endDay:
    # 获取所有CSV文件的列表
    csv_files = [file for file in os.listdir() if file.endswith('.csv') and file.startswith(str(startDay))]
    print(startDay)
    print(csv_files)

    # 初始化一个空的DataFrame来存储合并后的数据
    merged_data = pd.read_csv(csv_files[0], usecols=['External Order No.', 'Packaging Material Code', 'Manufct. Barcode', 'Pack Operator'])

    # 遍历所有CSV文件并将它们合并到merged_data DataFrame中
    for file in csv_files[1:]:
        data = pd.read_csv(file, usecols=['External Order No.', 'Packaging Material Code', 'Manufct. Barcode', 'Pack Operator'])
        merged_data = pd.concat([merged_data, data], ignore_index=True)

    # 将合并后的数据写入新的CSV文件
    merged_data.to_csv(str(startDay)+'-parcel.csv', index=False)

    startDay = (pd.Timestamp(startDay) + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
