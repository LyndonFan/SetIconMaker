import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_box(image,contours):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray",gray)
    cv2.waitKey(0)
    print(len(contours))
    im = gray
    im = np.pad(im, 20, constant_values=255)
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if cv2.contourArea(box) >= 25:
            print(box)
            cv2.drawContours(im,[box],0,(0,255,0),10,offset=(20,20))

    cv2.imshow("w/ box",im)
    cv2.waitKey(0)
    return box