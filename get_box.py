import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *

PAD_WIDTH = 20

def get_box(im,contours):

    print(len(contours))
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im = np.pad(im, PAD_WIDTH, constant_values=255)
    rects = []
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if cv2.contourArea(box) >= 25:
            print(box)
            rects.append(rect)
            #cv2.drawContours(im,[box],0,(0,255,0),10,offset=(PAD_WIDTH,PAD_WIDTH))
    
    print(rects)
    if len(rects)==0:
        #assert False, "No sufficiently large rectangles are found..."
        pass

    cv2.imshow("w/ box",gray)
    cv2.waitKey(0)
    return rect

def get_box_alt(im,contours):
    #im = np.pad(im, PAD_WIDTH, constant_values=255)
    flatten = lambda l: [item for sublist in l for item in sublist]
    points = np.array(flatten(contours))
    print(points)
    hull = cv2.convexHull(points)
    rect = cv2.minAreaRect(hull)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    if cv2.contourArea(box) >= 25:
        print(box)
        cv2.drawContours(im,[box],0,(0,255,0),10)
    cv2.imshow("w/ box",im)
    cv2.waitKey(0)
    return rect

if __name__ == "__main__":
    image = cv2.imread('test.png') 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    box = get_box(image,contours)

    image = cv2.imread('test2.png')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    box = get_box(image,contours)

    image = cv2.imread('test.png') 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    box = get_box_alt(image,contours)

    image = cv2.imread('test2.png')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    box = get_box_alt(image,contours)