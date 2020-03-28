import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *

PAD_WIDTH = 20

def get_box(im,contours):

    print(im.shape)
    flatten = lambda l: [item for sublist in l for item in sublist]
    #print(contours[0])
    points = np.array(flatten(flatten(contours)))
    #print(len(points),points[0])
    hull = cv2.convexHull(points)
    #print(hull)
    rect = cv2.minAreaRect(hull)
    print(rect)

    im_display = im.copy()
    cv2.polylines(im_display,[hull],True,thickness=10,color=(0,255,255),lineType=cv2.LINE_4)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print(box,type(box))
    cv2.drawContours(im_display,[box],-1,(0,255,0),10)
    cv2.imshow("w/ box",im_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rect

if __name__ == "__main__":
    image = cv2.imread('test.png') 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    get_box(image,contours)

    image_2 = cv2.imread('test2.png')
    gray_2 = cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)
    contours_2 = get_contours(image_2)
    get_box(image_2,contours_2)


