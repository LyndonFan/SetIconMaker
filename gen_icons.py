import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *
from get_icons import *
import sys

MAX_DIM = 600
PAD_WIDTH = 20

def gen_icons(raw_image,name="icon",stroke_width=10):
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
        trans_mask = resized[:,:,3] == 0
        resized[trans_mask] = [255, 255, 255, 255]
        no_alpha = cv2.cvtColor(resized, cv2.COLOR_BGRA2BGR)
    except:
        no_alpha = resized
    try:
        gray = cv2.cvtColor(no_alpha, cv2.COLOR_BGR2GRAY) # convert to grayscale
    except:
        gray = no_alpha
    blur = cv2.blur(gray, (10, 10)) # blur the image
    ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    padded = np.pad(thresh,PAD_WIDTH,mode="constant",constant_values=255)
    preprocessed = padded
    # cv2.imshow("preprocessed",preprocessed)
    # cv2.waitKey(0)
    contours = get_contours(preprocessed)
    obb = get_box(preprocessed,contours)
    all_icons = get_icons(preprocessed,contours,obb,stroke_width=stroke_width)
    for key in all_icons.keys():
        cv2.imwrite(name+key+".png",all_icons[key])

if __name__ == "__main__":
    args = sys.argv
    if len(args)==1:
        for i in range(1,5):
            name = "test"+str(i)
            image = cv2.imread(name+'.png')
            gen_icons(image,name)
    else:
        name = args[1]
        stroke_width = 10 if len(args)<=2 else int(args[2])
        image = cv2.imread(name, cv2.IMREAD_UNCHANGED)
        name = name.replace(".png","")
        gen_icons(image,name,stroke_width)