import datetime
import os

import pandas as pd
import pyautogui
import time
import xlrd
import pyperclip
from pynput.mouse import Button, Controller as c_mouse


# 编号1 双一拣
def searchMoveClick(img, x=0, y=0, clickNum=1):
    # 找到【异常分类】
    while True:
        try:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.moveTo(location.x * 0.5 + x, location.y * 0.5 + y)
                pyautogui.click(clicks=clickNum)
                time.sleep(1)
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print("未找到匹配图片,1秒后重试" + img)
            print('ImageNotFoundException: image not found')


def dataExport(pic_path, name):
    # 点击下拉菜单中的【任务管理】
    print("任务管理")
    img = os.path.join(pic_path, 'task_management.png')
    searchMoveClick(img, 0, 0, 1)

    # 点击下拉菜单中的【导出任务管理】
    print('导出任务管理')
    img = os.path.join(pic_path, 'export_task_management.png')
    searchMoveClick(img, 0, 0, 1)

    time.sleep(3)

    # 在文件名中搜索
    img = os.path.join(pic_path, 'inquire.png')
    searchMoveClick(img, -50, 0, 1)
    pyautogui.typewrite(name, interval=0.1)
    pyautogui.press('enter')

    # 点击【查询】
    while True:
        img = os.path.join(pic_path, 'inquire.png')
        searchMoveClick(img, 0, 0, 1)
        # 点击【下载】
        img = os.path.join(pic_path, 'downloadV2.png')

        imgNoData = os.path.join(pic_path, 'no_data.png')
        try:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.moveTo(location.x * 0.5, location.y * 0.5)
                pyautogui.click(clicks=1)
                time.sleep(1)
                break

        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print("未找到匹配图片,1秒后重试" + 'downloadV2.png')
            print('ImageNotFoundException: image not found')
        try:

            locationNoData = pyautogui.locateCenterOnScreen(imgNoData, confidence=0.9)
            if locationNoData is not None:
                print('没有查出数据，停掉程序')
                break
        except pyautogui.ImageNotFoundException:
            time.sleep(1)
            print("未找到匹配图片,1秒后重试" + 'no_data.png')



    time.sleep(2)

    pyautogui.typewrite(name, interval=0.1)
    # pyautogui.press('enter')
    time.sleep(1)

    # 选择保存目录
    img = os.path.join(pic_path, 'choice.png')
    searchMoveClick(img, 0, 0, 1)

    # 保存
    img = os.path.join(pic_path, 'save.png')
    searchMoveClick(img, 0, 0, 1)

if __name__ == '__main__':
    lOrR = 'left'
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    reTry = 1
    today = datetime.date.today()
    todaydiminish1 = (today + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    title = 'udyijm'
    concont = str(today) + title


    mouse = c_mouse()

    # 找到【库内】
    img = os.path.join(pic_path, '3-kunz.png')
    # mouseClick(2, lOrR, img, reTry)
    searchMoveClick(img, 0, 0, 2)

    # 找到【异常单】
    img = os.path.join(pic_path, '3-yiihdj.png')
    # mouseClick(1, lOrR, img, reTry)
    searchMoveClick(img, 0, 0, 1)

    # 找到【异常分类】
    img = os.path.join(pic_path, '3-yiihfflz.png')
    searchMoveClick(img, 50, 10, 1)

    # 等待2s
    time.sleep(2)

    # 下移30像素，找到少货并点击
    pyautogui.move(0, 30)
    pyautogui.click()

    # 找到【提交时间】
    img = os.path.join(pic_path, '3-tijcuijm.png')
    searchMoveClick(img, 40, 0, 1)

    # 找到【时间标记】
    img = os.path.join(pic_path, '3-uijmbcji.png')
    searchMoveClick(img, 0, -30, 1)

    time.sleep(1)
    pyautogui.hotkey('command', 'a')
    time.sleep(1)
    # 输入昨天的日期
    pyautogui.typewrite(todaydiminish1, interval=0.1)
    pyautogui.move(140, 0)

    # 原有的方法存在问题，无法点击，使用新的包
    mouse = c_mouse()
    mouse.click(Button.left, 2)
    # 输入 23 点
    pyautogui.typewrite('23', interval=0.1)

    # 找到【确定】
    img = os.path.join(pic_path, '3-qtdy.png')
    searchMoveClick(img, 0, 0, 1)
    # mouseClick(1, lOrR, img, reTry)
    time.sleep(1)

    # 找到【查询】
    img = os.path.join(pic_path, '3-iaxp.png')
    searchMoveClick(img, 0, 0, 1)
    # mouseClick(1, lOrR, img, reTry)
    time.sleep(3)

    # 找到【全部导出】
    img = os.path.join(pic_path, '3-qrbudkiu.png')
    searchMoveClick(img, 0, 0, 1)
    # mouseClick(1, lOrR, img, reTry)
    time.sleep(1)

    # 找到【任务名称】
    print("任务名称")
    img = os.path.join(pic_path, '3-rfwumyig.png')
    searchMoveClick(img, 0, 50, 1)

    time.sleep(1)
    pyautogui.typewrite(concont, interval=0.1)
    pyautogui.press('enter')

    # 找到【确定】
    print("确定")
    img = os.path.join(pic_path, '3-qtdy.png')
    searchMoveClick(img, 0, 0, 1)
    # mouseClick(1, lOrR, img, reTry)
    time.sleep(3)

    # ############################################################# 导出文件
    dataExport(pic_path, concont)


    csv_directory = '/Users/flash/LCP仓储/choice'
    columns_to_extract2 = ['Source LBX', 'Exception Type', 'Source Type', 'Created time']
    resultName='tmp_th_udyijm.xlsx'
    name = concont
    # 获取所有CSV文件
    csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv') and file.startswith(str(name))]

    file_paths = [os.path.join(csv_directory, file) for file in csv_files]
    print(file_paths)

    # 将文件中的 \, 字符去掉

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

    # 将udyijm的excel，取出需要的字段
    # 读取所有CSV文件并去除列名中的'.'，同时去除数据中的'`'字符
    dfs = []
    for file in csv_files:
        df = pd.read_csv(os.path.join(csv_directory, file), usecols=columns_to_extract2)
        # 去除列名中的'.'
        df.columns = [col.replace('.', '') for col in df.columns]
        # 去除数据中的'`'字符
        df = df.map(lambda x: str(x).replace('`', '') if isinstance(x, str) else x)
        df['today_date'] = today
        dfs.append(df)

    # 拼接所有DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # 写入到XLSX文件
    # combined_df.to_excel('/Users/flash/OneDrive/闪电快车/LCP/0422-3-拣货/tmp_th_combined_picked_data.xlsx', index=False)
    combined_df.to_excel(os.path.join(csv_directory, resultName), index=False)
    print("所有CSV文件已拼接并写入到'combined_data.xlsx'，列名中的'.'已被替换为''，数据中的'`'字符已被去除。")



