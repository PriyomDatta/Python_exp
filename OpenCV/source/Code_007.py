#capturing camera feed and mouse click data.

import numpy as np
import cv2

cap = cv2.VideoCapture(0)  #enables video feed

color = (0,255,0)          #green circle
line_width = 1             #width of radius -1 will fill the circle
radius = 100
point = (0,0)

#Event based function that will be called during click
def click(event, x, y, flags, param):
	global point
	if event == cv2.EVENT_LBUTTONUP:
		print("Pressed",x,y)
		point = (x,y)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click)  #enable mouse click event

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=1,fy=1)
	cv2.circle(frame, point, radius, color, line_width)     #Update circle location
	cv2.imshow("Frame",frame)

	ch = cv2.waitKey(1)                 #breaks loop
	if ch & 0xFF == ord('q'):
		break

#stops video capture
cap.release()
cv2.destroyAllWindows()