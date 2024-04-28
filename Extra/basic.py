import cv2 as cv
from rescale import rescaleFrame

img = cv.imread("Photos/sofia.jpg")
pic_resized = rescaleFrame(img,scale=.2)
cv.imshow("Sofia Resized", pic_resized)


# converting image to greyscale
# gray = cv.cvtColor(pic_resized, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# blur
blur = cv.GaussianBlur(pic_resized, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Find EdgeCascade
canny = cv.Canny(pic_resized, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dilated", dilated)

#Eroding
eroding = cv.erode(dilated, (3,3), iterations=1)
cv.imshow("Eroded", eroding)

#Resize
resized = cv.resize(pic_resized, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

#Cropping
cropped = pic_resized[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)