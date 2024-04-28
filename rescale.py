import cv2 as cv

# img = cv.imread("Photos/sofia")
# cv.imshow("Sofia", img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions= (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/sofia.jpg')

# cv.imshow("Sofia", img)

pic_resized = rescaleFrame(img,scale=.2)
cv.imshow("Sofia Resized", pic_resized)



cv.waitKey(0)