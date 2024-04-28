import cv2 as cv
import numpy as np
from rescale import rescaleFrame

img = cv.imread("Photos/sofia.jpg")
img = rescaleFrame(img,scale=.2)
cv.imshow("Sofia Resized", img)

# translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
cv.imshow("Translated", translated)
#47:27
cv.waitKey(0)