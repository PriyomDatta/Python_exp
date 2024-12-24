import numpy as np
import cv2

color = cv2.imread("../Images/butterfly.jpg",1)
cv2.imshow("Image",color)
cv2.moveWindow("Image",0,0)      #will put Image at top left corner
print(color.shape)
height,width,channels = color.shape  #gives shape

#We are going to create a image containing all the three splits(R,G,B)
b,g,r = cv2.split(color)

rgb_split = np.empty([height,width*3,3],'uint8') #init. height X 3*width image

rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels",rgb_split)
cv2.moveWindow("Channels",0,height)

# Same thing using HSV(Hue,Saturation,Value) split
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v),axis=1)     #Similat to merge concate is efficient
cv2.imshow("Split HSV",hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()