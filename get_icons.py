import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *

def get_icons(image,contours,obb):
    for x in "urm":
        background = cv2.imread(str(x)+".png")
        new_size = obb.shape
        M = cv2.getRotationMatrix2D(center=image.shape //2, angle = obb.angle)

if __name__ == "__main__":

'''
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # convert to grayscale
blur = cv2.blur(gray, (3, 3)) # blur the image
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
'''