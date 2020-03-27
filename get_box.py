import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *

def get_box(im,contours):

    print(len(contours))
    im = image
    im = np.pad(im, 20, constant_values=255)
    boxes = []
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if cv2.contourArea(box) >= 25:
            boxes.append(box)
            #print(box)
    
    if len(boxes)>=
            cv2.drawContours(im,[box],0,(0,255,0),10,offset=(20,20))

    cv2.imshow("w/ box",im)
    cv2.waitKey(0)
    return rect

if __name__ == "__main__":
    image = cv2.imread('test.png') 
    contours = get_contours(image)
    box = get_box(image,contours)

    image = cv2.imread('test2.png') 
    contours = get_contours(image)
    box = get_box(image,contours)