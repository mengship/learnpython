import datetime
import os

import pandas as pd
import pyautogui
import time
import xlrd
import pyperclip
from flash.zidshw.udyijm import searchMoveClick, dataExport
from pynput.mouse import Button, Controller as c_mouse
# 编号1 收货
if __name__ == '__main__':
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    today = datetime.date.today()
    todayadd1 = (today + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    title = 'consignees'
    concont = str(today) + title
    arrivalStart = '2023-01-01'
    arrivalEnd = str(todayadd1)
    notificationStart = '2023-12-01'
    # notificationEnd = str((today + datetime.timedelta(days=45)).strftime("%Y-%m-%d"))
    mouse = c_mouse()
    while notificationStart <= str(today):
        # notificationEnd:
        startDayAdd45 = (pd.Timestamp(notificationStart) + datetime.timedelta(days=45)).strftime("%Y-%m-%d")

        plannerName = str(today)+ 'plan order export' + startDayAdd45 + '3'
        plannerDetailName = str(today)+'plan order detail export' + startDayAdd45+'3'


        # 找到【入库】菜单
        img = os.path.join(pic_path, '7-入库.png')
        searchMoveClick(img, 0, 0, 2)

        # 找到【计划单】菜单
        img = os.path.join(pic_path, '7-计划单.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到 取消 时间过滤
        img = os.path.join(pic_path, '4-quxc.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【到仓时间】筛选项
        img = os.path.join(pic_path, '7-到仓时间.png')
        searchMoveClick(img, 50, 0, 1)
        pyautogui.click()

        pyautogui.typewrite(arrivalStart, interval=0.1)

        pyautogui.move(280, 0)
        pyautogui.click()

        pyautogui.typewrite(arrivalEnd, interval=0.1)

        # 找到【通知时间】筛选项
        img = os.path.join(pic_path, '7-通知时间.png')
        searchMoveClick(img, 50, 0, 1)
        pyautogui.click()

        pyautogui.typewrite(notificationStart, interval=0.1)

        pyautogui.move(280, 0)
        pyautogui.click()

        pyautogui.typewrite(startDayAdd45, interval=0.1)

        # 找到【查询】按钮
        img = os.path.join(pic_path, 'inquire.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【导出】按钮
        img = os.path.join(pic_path, '7-导出.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【导出计划单】按钮
        img = os.path.join(pic_path, '7-导出计划单.png')
        searchMoveClick(img, 0, 0, 1)

        img = os.path.join(pic_path, '7-导出名称.png')
        searchMoveClick(img, 0, 40, 1)

        mouse.click(Button.left, 3)
        pyautogui.typewrite(plannerName , interval=0.1)

        # 找到【确认】按钮
        img = os.path.join(pic_path, '7-确认.png')
        searchMoveClick(img, 0, 0, 1)

        time.sleep(1)

        # 找到【导出】按钮
        img = os.path.join(pic_path, '7-导出.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【导出计划单明细】按钮
        img = os.path.join(pic_path, '7-导出计划单明细.png')
        searchMoveClick(img, 0, 0, 1)
        time.sleep(3)

        img = os.path.join(pic_path, '7-导出名称.png')
        searchMoveClick(img, 0, 40, 1)

        mouse.click(Button.left, 3)
        pyautogui.typewrite(plannerDetailName, interval=0.1)
        # 找到【确认】按钮
        img = os.path.join(pic_path, '7-确认.png')
        searchMoveClick(img, 0, 0, 1)

        # 还少导出的部分
        dataExport(pic_path, plannerName)

        # 找到【库内】
        img = os.path.join(pic_path, '3-kunz.png')
        searchMoveClick(img, 0, 0, 2)

        # 找到【差异调整】
        img = os.path.join(pic_path, '5-iayitcvg.png')
        searchMoveClick(img, 0, 0, 1)

        time.sleep(3)

        dataExport(pic_path, plannerDetailName )


        notificationStart = startDayAdd45


        time.sleep(10)
        # 指定包含CSV文件的目录
    csv_directory = '/Users/flash/LCP仓储/choice'
    # 获取所有CSV文件
    today = datetime.date.today()
    name = str(today) + 'plan order export'
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name))]

    # 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(csv_directory, file))
        # 去除列名中的'.'
        df.columns = [col.replace('.', '') for col in df.columns]
        # 去除数据中的'`'字符
        df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
        # # 增加当日日期列
        # today = datetime.strftime('%Y-%m-%d')
        df['today_date'] = today
        dfs.append(df)

    # 拼接所有DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # 写入到XLSX文件
    combined_df.to_excel(os.path.join(csv_directory, 'tmp_th_combined_noreceipt_data0322.xlsx'), index=False)

    print("所有CSV文件已拼接并写入到'tmp_th_combined_noreceipt_data0322.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")

    # 指定包含CSV文件的目录
    csv_directory = '/Users/flash/LCP仓储/choice'
    today = datetime.date.today()
    name = str(today) + 'plan order detail export'
    # 获取所有CSV文件
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name))]

    # 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(csv_directory, file))
        # 去除列名中的'.'
        df.columns = [col.replace('.', '') for col in df.columns]
        # 去除数据中的'`'字符
        df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
        # # 增加当日日期列
        # today = datetime.now().strftime('%Y-%m-%d')
        df['today_date'] = today
        dfs.append(df)

    # 拼接所有DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # 写入到XLSX文件
    combined_df.to_excel(os.path.join(csv_directory, 'tmp_th_combined_noreceiptdetail_data0322.xlsx'), index=False)

    print("所有CSV文件已拼接并写入到'tmp_th_combined_noreceiptdetail_data0322.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")








