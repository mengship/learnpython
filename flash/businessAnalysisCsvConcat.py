# 菜鸟发的文件进行合并

#csv拼表，需要拼在一起的csv都放在一个单独的文件夹
import os
import glob
import pandas as pd
os.chdir(r"/Users/flash/OneDrive/闪电快车/LCP/202403对账")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#在列表中合并所有文件
combined_csv = pd.concat([pd.read_csv(f, encoding='gb2312') for f in all_filenames ])
#导出 csv
combined_csv.to_csv( "2024-03-clncorder.csv", index=False, encoding='utf-8-sig')
