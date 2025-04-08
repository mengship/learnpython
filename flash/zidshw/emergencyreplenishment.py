import datetime
import os

import pandas as pd
import pyautogui
import time
import xlrd
import pyperclip
from flash.zidshw.intercepted_Package_Detail import mouseClick

from pynput.mouse import Button, Controller as c_mouse
# 编号4 紧急补货任务数
from flash.zidshw.udyijm import searchMoveClick, dataExport

def main():
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    today = datetime.date.today()
    todaydiminish1 = (today + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    title = 'emergencyReplenishment'
    version = '1'
    concont = str(today) + title + version
    mouse = c_mouse()

    # 找到【库内】
    img = os.path.join(pic_path, '3-kunz.png')
    searchMoveClick(img, 0, 0, 2)

    # 找到【补货预测】
    img = os.path.join(pic_path, '4-buhoyuce.png')
    searchMoveClick(img, 0, 0, 1)

    time.sleep(3)

    # 向下滑动窗口
    pyautogui.scroll(-7)

    # 找到【日期取消】
    img = os.path.join(pic_path, '4-quxc.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【查询】
    img = os.path.join(pic_path, '4-iaxp.png')
    searchMoveClick(img, 0, 0, 1)
    time.sleep(7)

    # 向上滑动窗口
    pyautogui.scroll(7)
    time.sleep(1)

    # 找到【导出】
    img = os.path.join(pic_path, '4-dkiu.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【填写框】
    img = os.path.join(pic_path, '4-vuyi.png')
    searchMoveClick(img, 0, -25, 1)
    pyautogui.typewrite(concont, interval=0.1)
    pyautogui.press('enter')

    # 找到【确定】
    img = os.path.join(pic_path, '4-qtdy.png')
    searchMoveClick(img, 0, 0, 1)

    time.sleep(3)

    dataExport(pic_path, concont)

    time.sleep(10)

    # 库存转移
    # 指定包含CSV文件的目录
    csv_directory = '/Users/flash/LCP仓储/choice'
    out_directory = '/Users/flash/LCP仓储/choice/上传数据'
    columns_to_extract2 = ['行业',	'货主',	'商品名称',	'商品条码',	'商品类型',	'影响包裹数',	'影响商品数',	'拣选区可销售库存',	'待作业库存',	'来源库位',	'箱规',	'备货区库存',	'暂存区库存',	'预包区库存',	'正在补货数量',	'包装属性',	'商品ABC',	'托规',]
    # 获取所有CSV文件
    today = datetime.date.today()
    name = concont
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.xlsx') and file.startswith(str(name))]
    print(csv_files)
    # 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
    dfs = []
    for file in csv_files:
        df = pd.read_excel(os.path.join(csv_directory, file))
        # 选择特定的列
        selected_columns = df[columns_to_extract2]
        # 去除列名中的'.'
        selected_columns.columns = [col.replace('.', '') for col in selected_columns.columns]
        # 去除数据中的'`'字符
        selected_columns = selected_columns.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
        # df['today_date'] = today
        dfs.append(selected_columns)

    # 拼接所有DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # 写入到XLSX文件
    combined_df.to_excel(os.path.join(out_directory, 'tmp_th_ffm_lcp_urgent_supply.xlsx'), index=False)
    print("所有CSV文件已拼接并写入到'combined_data.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")

if __name__ == '__main__':
    main()