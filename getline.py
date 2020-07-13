import cv2 as cv
import numpy as np


def get_line(img):
    img = cv.resize(img, (500, 500))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.medianBlur(gray, 3)
    # 50,150 为二值化时的阈值 apertureSize为Sobel滤波器的大小
    edges = cv.Canny(blur, 75, 150, apertureSize=3)
    # 线条加粗
    imgTemp = np.zeros((500, 500), np.uint8)
    imgTemp[0:499, 0:500] = edges[1:500, 0:500]
    edges = cv.add(edges, imgTemp)
    imgTemp = np.zeros((500, 500), np.uint8)
    imgTemp[0:500, 0:499] = edges[0:500, 1:500]
    edges = cv.add(edges, imgTemp)
    imgTemp = np.zeros((500, 500), np.uint8)
    imgTemp[1:500, 0:500] = edges[0:499, 0:500]
    edges = cv.add(edges, imgTemp)
    imgTemp = np.zeros((500, 500), np.uint8)
    imgTemp[0:500, 1:500] = edges[0:500, 0:499]
    edges = cv.add(edges, imgTemp)
    # 反色
    cv.bitwise_not(edges, edges)
    # cv.imshow('Canny Result', edges)
    # cv.waitKey(0)
    return edges


def do_image():
    image = cv.imread('./temp/tmp.png')
    cv.imwrite('./temp/line.png', get_line(image))


if __name__ == '__main__':
    do_image()
