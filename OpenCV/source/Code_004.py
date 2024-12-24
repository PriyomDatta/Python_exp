import numpy as np
import cv2

color = cv2.imread("../Images/butterfly.jpg",1)

#converting to 1 scale image ie. gray
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("../Images/gray_004.jpg",gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

#Adding transparency over green ie. 4th param
rgba = cv2.merge((b,g,r,g))
cv2.imwrite("../Images/rgba_004.png",rgba)
