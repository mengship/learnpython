import datetime
import os
import pyautogui
import time
import xlrd
import pyperclip
from flash.zidshw.udyijm import searchMoveClick, dataExport


# 编号6 货主货位商品 少货待找回
def main():
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    today = datetime.date.today()
    title = 'missinggoodsrecovered'
    version = '2'
    concont = str(today) + title + version

    # 找到【台账】菜单
    img = os.path.join(pic_path, 'tlvh.png')
    searchMoveClick(img, 0, 0, 2)

    # 找到【货主货位商品】菜单
    img = os.path.join(pic_path, 'hovuhowzuhpn.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【库区】菜单
    img = os.path.join(pic_path, '6-库区.png')
    searchMoveClick(img, 50, 0, 1)

    pyautogui.move(0, 30)

    pyautogui.scroll(-5)

    # 找到【DEF】菜单
    img = os.path.join(pic_path, '6-DEF.png')
    searchMoveClick(img, -30, 0, 1)

    # 找到【LCP补货差异】菜单
    img = os.path.join(pic_path, '6-LCP补货差异.png')
    searchMoveClick(img, -30, 0, 1)

    # 找到【LCP补货差异】菜单
    img = os.path.join(pic_path, '6-W8补货差异.png')
    searchMoveClick(img, -30, 0, 1)

    # 找到【查询】按钮
    img = os.path.join(pic_path, 'inquire.png')
    searchMoveClick(img, 0, 0, 1)

    time.sleep(3)

    # 找到【导出】按钮
    img = os.path.join(pic_path, '6-导出.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【任务名称】按钮
    img = os.path.join(pic_path, '3-rfwumyig.png')
    searchMoveClick(img, 0, 50, 1)

    pyautogui.typewrite(concont, interval=0.1)

    # 找到【确定】按钮
    img = os.path.join(pic_path, '3-qtdy.png')
    searchMoveClick(img, 0, 0, 1)

    # 导出数据
    dataExport(pic_path, concont)


if __name__ == '__main__':
    main()
