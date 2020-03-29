import cv2
import numpy as np
from matplotlib import pyplot as plt
from math import *

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
    '''
    # Find Canny edges 
    edged = cv2.Canny(gray, 30, 200) 
    cv2.imshow("edges",edged)
    # Finding Contours 
    # Use a copy of the image e.g. edged.copy() 
    '''
    # since findContours alters the image 
    contours, hierarchy = cv2.findContours(gray.copy(),  
        cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    
    print("Number of Contours found = " + str(len(contours))) 
    print("Hierarchy:",hierarchy)

    new_image = np.ones(image.shape[:2]) * 255
    match_matrix = np.zeros((len(contours),len(contours)))
    M = []
    centroids = []
    for i in range(len(contours)):
        curr = cv2.drawContours(new_image.copy(), contours, i, (0, 0, 0), 5)
        #cv2.imshow("cnt",curr)
        cnt = contours[i]
        M.append(cv2.moments(cnt))
        centroids.append((int(M[-1]['m10']/M[-1]['m00']),int(M[-1]['m01']/M[-1]['m00'])))
        #print(i,centroids[-1],M[-1]["m00"])
        #cv2.waitKey(0)
    for i in range(len(contours)):
        for j in range(len(contours)):
            match_matrix[i,j] = abs(centroids[i][0]-centroids[j][0])+abs(centroids[i][1]-centroids[j][1])<=10 and abs(M[i]["m00"]-M[j]["m00"])/max(M[i]["m00"],M[j]["m00"])<=0.2 
            match_matrix[i,j] -= i==j
    #print(match_matrix) 
    contours_copy = []
    for i in range(len(contours)):
        if not(1 in match_matrix[i,:i] or cv2.moments(contours[i])["m00"]>=image.shape[0]*image.shape[1]*0.8):
            contours_copy.append(contours[i])
    #print(contours_copy)
    cv2.destroyAllWindows()
    return contours_copy

if __name__ == "__main__":
    image = cv2.imread('test.png') 
    contours = get_contours(image)

    image = cv2.imread('test2.png') 
    contours = get_contours(image)
