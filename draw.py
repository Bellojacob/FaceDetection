import cv2 as cv
import numpy as np
from rescale import rescaleFrame
img = cv.imread("Photos/sofia.jpg")
pic_resized = rescaleFrame(img,scale=.2)
# cv.imshow("Sofia Resized", pic_resized)

# create a blank canvas window
# blank = np.zeros((500,500,3), dtype="uint8")
# cv.imshow("Blank", blank)
# cv.rectangle(blank, (0,0), (250,250), (0,250,0), thickness=-1)
# cv.imshow("Rectangle", blank)

# blank[:] = 0,255,0
# cv.imshow("Green", blank)

#draw a circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
# cv.imshow("Circle", blank)

#draw a line
# cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
# cv.imshow("line", blank)

#write text on image
# cv.putText(blank, "Hello", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow("text",blank)

cv.rectangle(pic_resized, (400,100), (700,400), (0,0,255), thickness=3)
cv.imshow("Rectangle", pic_resized)

cv.putText(pic_resized,"Sofia", (500,430), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2 )
cv.imshow("Text", pic_resized)
cv.waitKey(0)