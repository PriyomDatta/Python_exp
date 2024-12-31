# Contour   their area, parameter and centroid
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

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')        #width x height x chanels  blank canvus

for c in contours:
	cv2.drawContours(objects, [c], -1, color, -1)

	area = cv2.contourArea(c)                                   # area is pixel^2
	perimeter = cv2.arcLength(c, True)                          #True means closed 

	M = cv2.moments(c)                                          #finds moment
	cx = int(M['m10'] / M['m00'])                               #centroid along x
	cy = int(M['m01'] / M['m00'])                               #centroid along y

	cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)           #drawing the centroid

	print(f"Area: {area}, perimeter: {perimeter}")              #printing

cv2.imshow("Contours_centroid", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
