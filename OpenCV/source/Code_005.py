#Blur, dilation and erosion

import numpy as np
import cv2

image = cv2.imread("../Images/thresh_005.jpg")
cv2.imshow("Original",image)

blur = cv2.GaussianBlur(image, (5,55),0)     #the (5,55) indicates that in x-axis the blur would be less and more in y-axis the following parameter should be odd.
cv2.imshow("Blur",blur)

kernel = np.ones((5,5),'uint8')   #defining karnel on which the next two operation will depend increasing will increase the effect

dilate = cv2.dilate(image,kernel,iterations=1)  #highlits white pixel 
erode = cv2.erode(image,kernel,iterations=1)    #highlits black pixel

cv2.imshow("Dilate",dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()