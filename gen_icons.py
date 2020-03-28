import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *
from get_icons import *

def gen_icons(raw_image):
    width, height = raw_image.shape[:2]
    new_width = 600 if width<=height else int(width*600/height)
    new_height = 600 if width>=height else int(height*600/width)
    resized = cv2.resize(raw_image,(new_width,new_height))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY) # convert to grayscale
    blur = cv2.blur(gray, (3, 3)) # blur the image
    ret, thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

    contours = get_contours(thresh)
    obb = get_box_alt(thresh)