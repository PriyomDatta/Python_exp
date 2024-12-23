import numpy as np
import cv2
img = cv2.imread("../Images/img_000.png")
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.imwrite("../Images/output_000.jpg",img)
exit()