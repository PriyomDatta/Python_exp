# Contour
import numpy as np
import cv2

img = cv2.imread('../Images/detect_blob.png',1)
cv2.imshow("Original", img)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)            #gray scale
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)    #adaptive threshold
cv2.imshow("Binary", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)          #Contour function

img2 = img.copy()                                       #deep copy so that original stays unaffected
index = -1                                              #all the contours
thickness = 1                                           
color = (255, 0, 255)                                   #pimk line

cv2.drawContours(img2, contours, index, color, thickness)   #draw the contours
cv2.imshow("Contours",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
