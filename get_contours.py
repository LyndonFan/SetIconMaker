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
    # Grayscale: assume input is grayscale
    gray = image    
    # Find Canny edges 
    edged = cv2.Canny(gray, 30, 200) 
    cv2.imshow("edges",edged)
    # Finding Contours 
    # Use a copy of the image e.g. edged.copy() 
    # since findContours alters the image 
    contours, hierarchy = cv2.findContours(edged.copy(),  
        cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    print("Number of Contours found = " + str(len(contours))) 
    print("Hierarchy:",hierarchy)

    new_image = np.ones(image.shape) * 255
    # Draw all contours 
    # -1 signifies drawing all contours 
    cv2.drawContours(new_image, contours, -1, (0, 0, 0), 5) 
    
    cv2.imshow("contours",new_image)
    cv2.waitKey(0)

    contours_copy = []
    hierarchy_copy = []
    for i in range(len(contours)):
        cnt = contours[i]
        if len(cnt)>=3:
            contours_copy.append(cnt)
            hierarchy_copy.append(hierarchy[0][i])
    return contours_copy, hierarchy_copy

if __name__ == "__main__":
    image = cv2.imread('test.png') 
    contours = get_contours(image)

    image = cv2.imread('test2.png') 
    contours = get_contours(image)
