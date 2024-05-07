import datetime
import os

import pandas as pd
import pyautogui
import time
import xlrd
import pyperclip
from flash.zidshw.udyijm import searchMoveClick, dataExport
# 编号3 货主货位商品 正品
if __name__ == '__main__':
    # lOrR = 'left'
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    # reTry = 1
    today = datetime.date.today()
    title = 'kuwzkucpuhpn'
    concont = str(today) + title

    # 找到【台账】菜单
    img = os.path.join(pic_path, 'tlvh.png')
    searchMoveClick(img, 0, 0, 2)

    # 找到【货主货位商品】菜单
    img = os.path.join(pic_path, 'hovuhowzuhpn.png')
    searchMoveClick(img, 0, 0, 1)

    pyautogui.moveTo(10 , 10)

    time.sleep(3)

    img = os.path.join(pic_path, 'stockstatus.png')
    searchMoveClick(img, 40, 0, 1)

    # 找到【正品选项】菜单
    img = os.path.join(pic_path, 'only_normal.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【查询】按钮
    img = os.path.join(pic_path, 'inquire.png')
    searchMoveClick(img, 0, 0, 1)

    time.sleep(3)

    # 找到【导出】按钮
    img = os.path.join(pic_path, 'export.png')
    searchMoveClick(img, 0, 0, 1)

    pyautogui.typewrite(concont, interval=0.1)
    pyautogui.press('enter')

    # 找到【确定】按钮
    img = os.path.join(pic_path, 'sure.png')
    searchMoveClick(img, 0, 0, 1)

    time.sleep(2)

    # 文件导出
    dataExport(pic_path, concont)

    time.sleep(6)

    csv_directory = '/Users/flash/LCP仓储/choice'
    # columns_to_extract2 = ['Source LBX', 'Exception Type', 'Source Type', 'Created time']
    resultName = 'tmp_th_kuwzkucpuhpn.xlsx'
    name = concont
    # 获取所有CSV文件
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name))]
    print('csv_files'+str(csv_files))

    file_paths = [os.path.join(csv_directory, file) for file in csv_files]
    print('file_paths'+str(file_paths))

    # 将文件中的 \, 字符去掉

    # 尝试使用不同的编码读取文件
    encodings = ['utf-8', 'gbk', 'utf-16', 'utf-16le', 'utf-16be', 'latin1']

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

    # 需要等待10s钟，不能立马去读，会出错
    time.sleep(30)
    # 将商品货主货位的excel，取出需要的字段
    # 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
    dfs = []
    for file in csv_files:
        print('file'+file)
        # 读取文件内容
        for encoding in encodings:
            try:
                df = pd.read_csv(os.path.join(csv_directory, file), encoding=encoding)
                # 获取列名列表
                column_names = df.columns.tolist()
                # 导出时，列名有的时候会出错zone Zone，这里强制转成我们需要的列名
                N1 = 8
                N2 = 9
                # 修改列名
                df.rename(columns={column_names[N1]: '库区'}, inplace=True)
                df.rename(columns={column_names[N2]: '库位'}, inplace=True)

                # 去除列名中的'.'
                df.columns = [col.replace('.', '') for col in df.columns]
                # 去除数据中的'`'字符
                df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
                df['today_date'] = today
                dfs.append(df)
                # print(dfs)
                break
            except UnicodeDecodeError:
                print(f"Failed with encoding: {encoding}")


    # print('out dfs'+str(dfs))
    # 拼接所有DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # 写入到XLSX文件
    combined_df.to_excel(os.path.join(csv_directory, resultName), index=False)
    print("所有CSV文件已拼接并写入到'combined_data.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")





