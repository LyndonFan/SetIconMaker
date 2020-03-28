import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *
from get_icons import *
import sys

MAX_DIM = 600
PAD_WIDTH = 20

def gen_icons(raw_image,name="icon"):
    width, height = raw_image.shape[:2]
    if width>=height:
        new_width = MAX_DIM
        new_height = int(height*MAX_DIM/width)
    else:
        new_height = MAX_DIM
        new_width = int(width*MAX_DIM/height)
    print((width,height),(new_width,new_height))
    resized = cv2.resize(raw_image,dsize=(new_height,new_width))
    try:
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) # convert to grayscale
    except:
        gray = resized
    blur = cv2.blur(gray, (10, 10)) # blur the image
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    padded = np.pad(thresh,PAD_WIDTH,mode="constant",constant_values=255)
    preprocessed = padded
    '''
    cv2.imshow("preprocessed",preprocessed)
    cv2.waitKey(0)
    '''
    contours = get_contours(preprocessed)
    obb = get_box(preprocessed,contours)
    get_icons(preprocessed,contours,obb,name)

if __name__ == "__main__":
    args = sys.argv
    if len(args)==1:
        for i in range(1,5):
            name = "test"+str(i)
            image = cv2.imread(name+'.png')
            gen_icons(image,name)
    else:
        for name in args[1:]:
            image = cv2.imread(name+'.png')
            gen_icons(image,name)