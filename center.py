import numpy as np
import cv2 
import imutils

image = cv2.imread('C:/Users/Diego/Documents/python/ROBOTICA/Proyecto/img.jpg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 130, 255, 0)

cnts = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]  
cntsSorted = sorted(cnts, key=cv2.contourArea)

for c in cntsSorted:
    
    contourImg = cv2.drawContours(image, [c], -1, (0,255,0), 3)
    cv2.imshow("Contours", contourImg)

    cv2.waitKey(0)
