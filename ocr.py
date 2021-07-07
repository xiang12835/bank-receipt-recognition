# coding=utf-8

import pytesseract
from PIL import Image
import sys


def run(image_path):

    # 打开图片
    image = Image.open(image_path)

    # 转为灰度图片
    imgry = image.convert('L')

    # 二值化，采用阈值分割算法，threshold为分割点,根据图片质量调节
    threshold = 150
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)

    temp = imgry.point(table, '1')

    # OCR识别：lang指定中文,--psm 6 表示按行识别，有助于提升识别准确率
    text = pytesseract.image_to_string(temp, lang="chi_sim+eng", config='--psm 6')

    # 打印识别后的文本
    # print(text)

    return text

if __name__ == "__main__":

    try:
        arg1 = sys.argv[1]
        print run(arg1)
    except IndexError:
        print('''Please input image path!\nlike:\npython ocr.py test1.jpg''')



