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
    #(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)