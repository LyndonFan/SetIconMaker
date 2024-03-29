import cv2
import numpy as np
from matplotlib import pyplot as plt
from get_contours import *
from get_box import *
import os

CWD = os.path.dirname(os.path.abspath(__file__))


def get_icons(image, contours, obb, angle="auto", stroke_width=10):

    box = cv2.boxPoints(obb)
    box = np.int0(box)

    opp_dist = sqrt((box[0][0] - box[2][0])**2 + (box[0][1] - box[2][1])**2)

    all_icons = {}

    if type(angle) == str:
        angle = obb[-1] - 90

    for x in "URM":
        im = image
        background = cv2.imread(os.path.join(CWD, str(x)+".png"))
        M_rot = cv2.getRotationMatrix2D(
            center=(background.shape[0]/2, background.shape[1]/2),
            angle=angle,
            scale=max(opp_dist/background.shape[0],
                      opp_dist/background.shape[1])
        )
        rot_background = cv2.warpAffine(
            background, M_rot, background.shape[:2])
        M_trans = np.float32(
            [[1, 0, obb[0][0]-background.shape[0]/2], [0, 1, obb[0][1]-background.shape[1]/2]])
        trans_background = cv2.warpAffine(
            rot_background, M_trans, (image.shape[1], image.shape[0]))

        # display = trans_background.copy()
        # cv2.drawContours(display,[box],-1,(0,0,0),1)
        # cv2.circle(display,tuple(map(int,obb[0])),2,(0,0,0),4)
        # cv2.imshow(x,display)
        # cv2.waitKey(0)

        im = im.reshape(image.shape[0], image.shape[1], 1)
        # print(im.shape)
        im = np.repeat(im, repeats=3, axis=2)
        # print(im.shape)
        # print(trans_background.shape)
        im = cv2.bitwise_not(im)
        res = cv2.bitwise_and(im, trans_background)
        im = cv2.bitwise_not(im)
        # cv2.imshow(x,res)
        res = cv2.bitwise_or(im, trans_background)
        cv2.drawContours(res, contours, -1, (0, 0, 0), stroke_width)
        '''
        cv2.imshow(x,res)
        cv2.waitKey(0)
        '''
        # cv2.imwrite(name+x+".png",res)
        all_icons[x] = res

    common = np.ones(image.shape) * 255
    cv2.drawContours(common, contours, -1, (0, 0, 0), stroke_width)
    # cv2.imwrite(name+"C.png",common)
    all_icons["C"] = common

    common_alt = np.ones(image.shape) * 255
    cv2.drawContours(common_alt, contours, -1, (0, 0, 0), -1)
    # cv2.imwrite(name+"C_alt.png",common_alt)
    all_icons["C_alt"] = common_alt

    return all_icons


if __name__ == "__main__":
    image = cv2.imread('test2.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    obb = get_box(image, contours)
    get_icons(gray, contours, obb)

    image = cv2.imread('test.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contours = get_contours(image)
    obb = get_box(image, contours)
    get_icons(gray, contours, obb)
