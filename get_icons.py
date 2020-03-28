import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *

def get_icons(image,contours,obb,name="icon"):
    
    box = cv2.boxPoints(obb)
    box = np.int0(box)

    for x in "URM":
        im = image
        background = cv2.imread(str(x)+".png")
        M_rot = cv2.getRotationMatrix2D(center=(background.shape[0]/2,background.shape[1]/2), angle = obb[-1]/np.pi*180 - 90,scale=1)
        rot_background = cv2.warpAffine(background,M_rot,background.shape[:2])
        M_trans = np.float32([[1,0,obb[0][0]-background.shape[0]/2],[0,1,obb[0][1]-background.shape[1]/2]])
        trans_background = cv2.warpAffine(rot_background,M_trans,(image.shape[1],image.shape[0]))
        display = trans_background.copy()
        cv2.drawContours(display,[box],-1,(0,0,0),1)
        cv2.circle(display,tuple(map(int,obb[0])),2,(0,0,0),4)
        cv2.imshow(x,display)
        cv2.waitKey(0)

        im = im.reshape(image.shape[0],image.shape[1],1)
        #print(im.shape)
        im = np.repeat(im,repeats=3,axis=2)
        #print(im.shape)
        #print(trans_background.shape)
        im = cv2.bitwise_not(im)
        res = cv2.bitwise_and(im,trans_background)
        im = cv2.bitwise_not(im)
        cv2.imshow(x,res)
        res = cv2.bitwise_or(im,trans_background)
        cv2.drawContours(res,contours,-1,(0,0,0),10)
        cv2.imshow(x,res)
        cv2.waitKey(0)

        cv2.imwrite(name+x+".png",res)
        

if __name__ == "__main__":
    image = cv2.imread('test2.png') 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    obb = get_box(image,contours)
    get_icons(gray,contours,obb)

    image = cv2.imread('test.png') 
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    obb = get_box(image,contours)
    get_icons(gray,contours,obb)