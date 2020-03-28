import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *
from get_icons import *

def gen_icons(raw_image,name="icon"):
    width, height = raw_image.shape[:2]
    if width>=height:
        new_width = 600
        new_height = int(height*600/width)
    else:
        new_height = 600
        new_width = int(width*600/height)
    print((width,height),(new_width,new_height))
    resized = cv2.resize(raw_image,dsize=(new_height,new_width))
    try:
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) # convert to grayscale
    except:
        gray = resized
    blur = cv2.blur(gray, (5, 5)) # blur the image
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

    cv2.imshow("threshed",thresh)
    cv2.waitKey(0)
    contours = get_contours(thresh)
    obb = get_box(thresh,contours)
    get_icons(thresh,contours,obb,name)

if __name__ == "__main__":
    image = cv2.imread('test2.png')
    gen_icons(image,"test2")

    image = cv2.imread('test.png')
    gen_icons(image,"test")