import os
import glob

# 设置要处理的文件夹路径
folder_path = '/Users/flash/LCP仓储/临时目录'

# 获取文件夹中所有.txt文件的路径
file_paths = glob.glob(os.path.join(folder_path, '*.csv'))

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

print("所有文件处理完成。")
