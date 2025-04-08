import datetime
import os

import pyautogui
import time
import xlrd
import pyperclip

from flash.zidshw.udyijm import searchMoveClick


# 编号2 异常单据
def mouseClick(clickTimes, lOrR, img, reTry):
    if reTry == 1:
        while True:
            try:
                location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                if location is not None:
                    # pyautogui.moveTo(location.x * 0.5, location.y * 0.5)
                    # pyautogui.sleep(1)
                    pyautogui.click(location.x * 0.5, location.y * 0.5, clicks=clickTimes, interval=0.5, duration=0,
                                    button=lOrR)
                    break
                print("未找到匹配图片,0.1秒后重试")
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print('ImageNotFoundException: image not found')

    elif reTry == -1:
        while True:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
            time.sleep(0.1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
            if location is not None:
                pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
                print("重复")
                i += 1
            time.sleep(0.1)


def main():
    pic_path = '/Users/flash/PycharmProjects/learnpython/flash/zidshw'
    today = datetime.date.today()
    title = 'intercepted_Package_Detail'
    version = '1'
    concont = str(today) + title + version

    # 找到【数据】菜单
    img = os.path.join(pic_path, 'logo_data.png')
    searchMoveClick(img, 0, 0, 2)

    time.sleep(2)

    # 找到【TIDA】菜单
    img = os.path.join(pic_path, 'logo_tida.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【出库管理】菜单
    img = os.path.join(pic_path, 'outControl.png')
    searchMoveClick(img, 0, 0, 1)

    # 找到【packageofinter】菜单
    img = os.path.join(pic_path, 'packageofinter.png')
    searchMoveClick(img, 0, 0, 1)

    pyautogui.sleep(5)

    # 找到【过滤】标记
    img = os.path.join(pic_path, 'filter1.png')
    searchMoveClick(img, 0, 0, 1)

    # 清除时间
    img = os.path.join(pic_path, 'qyiu.png')
    searchMoveClick(img, 0, 0, 1)

    # 下载数据
    img = os.path.join(pic_path, 'download.png')
    searchMoveClick(img, 0, 0, 1)

    pyautogui.scroll(-5)

    # 点击OK
    img = os.path.join(pic_path, 'ok.png')
    searchMoveClick(img, 0, 0, 1)

    # 10s等待弹窗出现
    time.sleep(10)

    pyautogui.typewrite(concont, interval=0.1)
    # pyautogui.press('enter')

    # 选择保存目录
    img = os.path.join(pic_path, 'choice.png')
    searchMoveClick(img, 0, 0, 1)

    # 保存
    img = os.path.join(pic_path, 'save.png')
    searchMoveClick(img, 0, 0, 1)

    csv_directory = '/Users/flash/LCP仓储/choice'
    out_directory = '/Users/flash/LCP仓储/choice/上传数据'
    xlsxName = 'tmp_th_intercepted_Package_Detail_Package_Detail.xlsx'
    xlsxNameAbsolute = os.path.join(csv_directory, xlsxName)

    # 检查文件是否存在
    if os.path.exists(xlsxNameAbsolute):
        # 删除文件
        os.remove(xlsxNameAbsolute)
        print(f"File '{xlsxNameAbsolute}' has been deleted.")
    else:
        print(f"File '{xlsxNameAbsolute}' does not exist.")

    xlsxNameAbsolute = os.path.join(out_directory, xlsxName)

    old_file_name = os.path.join(csv_directory, concont + '.xlsx')

    # 检查文件是否存在
    if os.path.exists(old_file_name):
        # 重命名文件
        os.rename(old_file_name, xlsxNameAbsolute)
        print(f"File '{old_file_name}' has been renamed to '{xlsxNameAbsolute}'.")
    else:
        print(f"File '{old_file_name}' does not exist.")


if __name__ == '__main__':
    main()
