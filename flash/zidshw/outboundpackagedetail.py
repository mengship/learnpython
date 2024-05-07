import datetime
import os

import pandas as pd
import pyautogui
import time
import xlrd
import pyperclip
from flash.zidshw.udyijm import searchMoveClick, dataExport
from pynput.mouse import Button, Controller as c_mouse

# 编号8 出库包裹明细
if __name__ == '__main__':
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    today = datetime.date.today()
    title = 'outboundpackagedetail'
    concont = str(today) + title
    today = datetime.date.today()
    todaydiminish1 = (today + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    todaydiminish2 = (today + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
    # todaydiminish3 = (today + datetime.timedelta(days=-3)).strftime("%Y-%m-%d")
    version = 7
    startHour = ['23', '7', '15']
    endHour = ['7', '15', '23']
    # 2024-05-01 23 ~ 2024-05-02 7
    # 2024-05-02 7 ~ 2024-05-02 15
    # 2024-05-02 15 ~ 2024-05-02 23
    startDate = [str(todaydiminish2) , str(todaydiminish1) , str(todaydiminish1) ]
    endDate = [str(todaydiminish1), str(todaydiminish1), str(todaydiminish1)]

    for i in [1, 2, 3]:
        # 找到【出库】菜单
        img = os.path.join(pic_path, '8-出库菜单.png')
        searchMoveClick(img, 0, 0, 2)

        # 找到【包裹查询】菜单
        img = os.path.join(pic_path, '8-包裹查询.png')
        searchMoveClick(img, 0, 0, 1)

        time.sleep(3)

        # 找到【展开】按钮
        img = os.path.join(pic_path, '8-展开.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【创建时间】菜单
        img = os.path.join(pic_path, '8-创建时间.png')
        searchMoveClick(img, 360, 0, 1)

        # 找到【发货时间】菜单
        img = os.path.join(pic_path, '8-发货时间.png')
        searchMoveClick(img, 60, 0, 1)

        # 找到【时间标记】
        img = os.path.join(pic_path, '8-时间标记.png')
        searchMoveClick(img, 0, -30, 1)

        # 原有的方法存在问题，无法点击，使用新的包
        mouse = c_mouse()
        mouse.click(Button.left, 2)

        time.sleep(1)
        # 输入2天前的日期
        pyautogui.typewrite(startDate[i-1], interval=0.1)
        pyautogui.move(140, 0)

        mouse.click(Button.left, 2)
        # 输入 23 点
        pyautogui.typewrite(startHour[i-1], interval=0.1)

        # 找到第二个日期输入框
        pyautogui.move(160, 0)

        mouse.click(Button.left, 2)

        time.sleep(1)
        # 输入2天前的日期
        pyautogui.typewrite(endDate[i-1], interval=0.1)
        pyautogui.move(140, 0)

        mouse.click(Button.left, 2)
        # 输入 23 点
        pyautogui.typewrite(endHour[i-1], interval=0.1)


        # 找到【确定】
        img = os.path.join(pic_path, '8-确定.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【搜索】
        img = os.path.join(pic_path, '8-搜索.png')
        searchMoveClick(img, 0, 0, 1)

        time.sleep(6)

        # 找到【详情导出】
        img = os.path.join(pic_path, '8-详情导出.png')
        searchMoveClick(img, 0, 0, 1)

        # 找到【详情导出】
        img = os.path.join(pic_path, '8-请填写任务名称.png')
        searchMoveClick(img, 0, 30, 1)

        # 输入导出文件名
        pyautogui.typewrite(str(todaydiminish1)+title+str(version)+str(i), interval=0.1)

        # 找到【确定2】
        img = os.path.join(pic_path, '8-确定2.png')
        searchMoveClick(img, 0, 0, 1)

        dataExport(pic_path, str(todaydiminish1)+title+str(version)+str(i))
        time.sleep(3)

    time.sleep(15)

    # 将三个文档合并到一起，输出到excel中
    # 指定包含CSV文件的目录
    csv_directory = '/Users/flash/LCP仓储/choice'
    today = datetime.date.today()
    todaydiminish1 = (today + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    name = str(todaydiminish1) + 'outboundpackagedetail'
    # 获取所有CSV文件
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name))]

    # 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(csv_directory, file))
        # 去除列名中的'.'
        df.columns = [col.replace('.', '') for col in df.columns]
        df.columns = [col.replace(':', '') for col in df.columns]
        df.columns = [col.replace('(', '') for col in df.columns]
        df.columns = [col.replace(')', '') for col in df.columns]
        # 去除数据中的'`'字符
        df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
        # df = df.map(lambda x: str(x).replace(':', '') if isinstance(x, str) else x)
        # df = df.map(lambda x: str(x).replace('(', '') if isinstance(x, str) else x)
        # df = df.map(lambda x: str(x).replace(')', '') if isinstance(x, str) else x)
        # # 增加当日日期列
        # today = datetime.now().strftime('%Y-%m-%d')
        df['today_date'] = todaydiminish1
        dfs.append(df)

    # 拼接所有DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # 写入到XLSX文件
    combined_df.to_excel(os.path.join(csv_directory, 'tmp_th_combined_parcel_detail.xlsx'), index=False)

