#more threshold and their combination

import numpy as np
import cv2

img = cv2.imread('../Images/faces.jpeg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)      #load the image in hsv

#seperating the chanels
h = hsv[:,:,0]      #hue is a circular parameter
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v), axis=1)     #concatinate and show image in hsv
cv2.imshow("Split HSV",hsv_split)

ret, min_sat = cv2.threshold(s,40,255, cv2.THRESH_BINARY)       #A threshold filter on saturation
cv2.imshow("Sat Filter",min_sat)

ret, max_hue = cv2.threshold(h,15, 255, cv2.THRESH_BINARY_INV)  #An inverse threshold filter on hue
cv2.imshow("Hue Filter",max_hue)

final = cv2.bitwise_and(min_sat,max_hue)                        #combining the two filtered image
cv2.imshow("Final",final)
cv2.imshow("Original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
