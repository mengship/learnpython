import datetime
import os

import pandas as pd
import pyautogui
import time
import xlrd
import pyperclip
from pynput.mouse import Button, Controller as c_mouse
from flash.zidshw.udyijm import searchMoveClick, dataExport

# 编号5 积压单昨日取消
if __name__ == '__main__':
    lOrR = 'left'
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    reTry = 1
    startDay='2024-03-01'
    today = datetime.date.today()
    todayadd10 = (today + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    print(todayadd10)
    title = 'Backlogabolish'
    concont = str(today) + title

    mouse = c_mouse()

    while startDay <= str(today):
        startDayAdd45 = (pd.Timestamp(startDay) + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
        name = concont + startDay + '~' + startDayAdd45 + '3'

        # 找到【库内】
        img = os.path.join(pic_path, '3-kunz.png')
        searchMoveClick(img, 0, 0, 2)

        # 找到【差异调整】
        img = os.path.join(pic_path, '5-iayitcvg.png')
        searchMoveClick(img, 0, 0, 1)

        time.sleep(3)

        # 找到【状态】
        img = os.path.join(pic_path, '5-status.png')
        searchMoveClick(img, 50, 0, 1)
        time.sleep(2)
        pyautogui.move(0, 175)
        pyautogui.click(clicks=1)

        # 找到【创建时间】
        img = os.path.join(pic_path, '5-idjmuijm.png')
        searchMoveClick(img, 50, 0, 1)
        pyautogui.move(0, 50)
        pyautogui.click(clicks=1)
        mouse.click(Button.left, 3)
        pyautogui.typewrite(startDay, interval=0.1)
        pyautogui.move(400, 0)
        pyautogui.click(clicks=1)
        mouse.click(Button.left, 3) # 左键连点三次
        pyautogui.typewrite(startDayAdd45, interval=0.1)

        # 找到【搜索】
        img = os.path.join(pic_path, '5-搜索.png')
        searchMoveClick(img, 0, 0, 1)

        time.sleep(10)

        # 找到【导出】
        img = os.path.join(pic_path, '5-导出.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【任务名称】
        img = os.path.join(pic_path, '5-任务名称.png')
        searchMoveClick(img, 0, 50, 1)
        pyautogui.typewrite(name , interval=0.1)
        pyautogui.press('enter')

        while True:
            # 找到【确定】
            img = os.path.join(pic_path, '5-确定.png')
            searchMoveClick(img, 0, 0, 1)

            # 点击【下载】
            img = os.path.join(pic_path, '有任务正在下载.png')
            try:
                location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                if location is not None:
                    pyautogui.moveTo(location.x * 0.5, location.y * 0.5)
                    print("有任务正在下载" + '有任务正在下载.png，等待3s')
                    time.sleep(3)
            except pyautogui.ImageNotFoundException:
                break
                # break

        dataExport(pic_path, name)

        time.sleep(3)

        startDay = startDayAdd45

    time.sleep(10)

    csv_directory = '/Users/flash/LCP仓储/choice'
    todaydiminish1 = (today + datetime.timedelta(days=-1))
    print(todaydiminish1)
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(concont))]
    DataSatisfyConditions = 0
    for file in csv_files:
        # 循环读取csv文件
        df = pd.read_csv(os.path.join(csv_directory, file) ,low_memory=False)
        # 假设我们要筛选列名为'Column_Name'的列，条件是值大于某个值
        # condition = df['Last modified time'] > '2024-04-29'
        df['Last modified time'] = pd.to_datetime(df['Last modified time'])

        # 筛选满足条件的行
        filtered_df = df[df['Last modified time'].dt.date == todaydiminish1]
        # print(df['Last modified time'].dt.date)

        # 输出筛选后的行数
        print('文件名称'+file)
        print("满足条件的行数：", len(filtered_df))
        DataSatisfyConditions += len(filtered_df)


    print(DataSatisfyConditions)

    DataCreateConditions = 0
    for file in csv_files:
        # 循环读取csv文件
        df = pd.read_csv(os.path.join(csv_directory, file) ,low_memory=False)
        # 假设我们要筛选列名为'Column_Name'的列，条件是值大于某个值
        # condition = df['Last modified time'] > '2024-04-29'
        df['Creation time'] = pd.to_datetime(df['Creation time'])
        df['Last modified time'] = pd.to_datetime(df['Last modified time'])

        # 筛选满足条件的行
        df = df[df['Creation time'].dt.date == todaydiminish1]
        filtered_df = df[df['Last modified time'].dt.date == todaydiminish1]
        # print(df['Last modified time'].dt.date)

        # 输出筛选后的行数
        print('文件名称'+file)
        print("满足条件的行数：", len(filtered_df))
        DataCreateConditions += len(filtered_df)

    print(DataCreateConditions)