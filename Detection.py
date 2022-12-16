import cv2
 
img = cv2.imread('C:/Users/Diego/Documents/python/ROBOTICA/Proyecto/imagen3.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',img.shape)
 
cv2.imshow("Resized image", img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 75, 255, 0)

cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnt = sorted(cnts, key=cv2.contourArea)





for c in cnt:
    # compute the center of the contoxur
    M = cv2.moments(c)
    try: 
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    except:
        pass
    
    cv2.drawContours(img,[c], 0, (0,255,0), 3)
    cv2.circle(img, (cX, cY), 7, (0, 0, 255), -1)

    
cv2.imshow("result", img)
cv2.waitKey(0)

