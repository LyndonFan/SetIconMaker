import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *

PAD_WIDTH = 20

def get_box(im,contours):

    im_padded = im
    print(im_padded.shape)
    im_padded = np.pad(im, ((PAD_WIDTH,PAD_WIDTH),(PAD_WIDTH,PAD_WIDTH),(0,0)), constant_values=255)

    flatten = lambda l: [item for sublist in l for item in sublist]
    print(contours[0])
    points = np.array(flatten(flatten(contours)))
    print(len(points),points[0])
    hull = cv2.convexHull(points)
    #print(hull)
    cv2.polylines(im_padded,[hull],True,thickness=5,color=(0,255,255))
    rect = cv2.minAreaRect(hull)
    print(rect)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    if cv2.contourArea(box) >= 25:
        print(box,type(box))
        cv2.drawContours(im_padded,[box],-1,(0,255,0),10,offset=(PAD_WIDTH,PAD_WIDTH))
    cv2.imshow("w/ box",im_padded)
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


