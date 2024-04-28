import cv2 as cv

from rescale import rescaleFrame

img = cv.imread("Photos/sofia.jpg")
img = rescaleFrame(img,scale=.2)
cv.imshow("Sofia Resized", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny= cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.waitKey(0)
