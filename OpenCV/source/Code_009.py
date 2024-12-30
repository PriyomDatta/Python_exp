#Example of threshold
import numpy as np
import cv2

bw = cv2.imread('../Images/detect_blob.png', 0)	#load the image as black and white
height, width = bw.shape[0:2]					#get dimention
cv2.imshow("Original BW",bw)					#diaplay the image

binary = np.zeros([height,width,1],'uint8')		#create ome chanel binary image

thresh = 85										#set threshold

for row in range(0,height):
	for col in range(0, width):
		if bw[row][col]>thresh:
			binary[row][col]=255

cv2.imshow("Slow Binary",binary)

ret, thresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)	#build in function in openCV for threshold
print(ret)
cv2.imshow("CV Threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()