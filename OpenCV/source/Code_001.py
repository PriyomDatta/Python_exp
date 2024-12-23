import numpy as np
import cv2
img = cv2.imread("../Images/img_000.png",1) #cv2.IMREAD_COLOR need to try 0 will be black & white 
print(img)
print(type(img))
print(len(img[0]))
print(len(img[0][0]))
print(img.shape)
print(img.dtype)

print(img[0, 930]) #0 0 0 ie. black
print(img[:,:,0])
print(img.size)