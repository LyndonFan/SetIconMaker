import cv2
import numpy as np
from matplotlib import pyplot as plt


def remove_noise(gray, num):
    Y, X = gray.shape
    nearest_neigbours = [[
        np.argmax(
            np.bincount(
                gray[max(i - num, 0):min(i + num, Y), max(j - num, 0):min(j + num, X)].ravel()))
        for j in range(X)] for i in range(Y)]
    result = np.array(nearest_neigbours, dtype=np.uint8)
    #cv2.imwrite('result2.jpg', result)
    return result

def get_contours(image):    
    # Grayscale 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    # Find Canny edges 
    edged = cv2.Canny(gray, 30, 200) 
    
    # Finding Contours 
    # Use a copy of the image e.g. edged.copy() 
    # since findContours alters the image 
    contours, hierarchy = cv2.findContours(edged,  
        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    
    cv2.imshow("original",image)
    cv2.waitKey(0)
    
    print("Number of Contours found = " + str(len(contours))) 

    new_image = np.ones(image.shape) * 255
    # Draw all contours 
    # -1 signifies drawing all contours 
    cv2.drawContours(new_image, contours, -1, (0, 0, 0), 5) 
    
    cv2.imshow("contours",new_image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    des = cv2.bitwise_not(gray)
    contours,hier = cv2.findContours(des,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours_copy = []
    for cnt in contours:
        if len(cnt) >=3:
            cv2.drawContours(des,[cnt],0,255,-1)
            contours_copy.append(cnt)
    return contours_copy

if __name__ == "__main__":

    image = cv2.imread('/Users/lyndonf/Desktop/Entertainment/MTG/DIYs/Raw (Don\'t delete)/Dromoka.png') 

    contours = get_contours(image)
    gray = cv2.bitwise_not(des)

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
    '''
    im2 = np.ones(im.shape) * 255
    cv2.drawContours(im2,[box],0,(0,0,0),-1)

    cv2.imshow("w/ box",im2)
    cv2.waitKey(0)
    '''
