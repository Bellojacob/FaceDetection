import cv2 as cv

# img = cv.imread('Photos/sofia.jpg')

# cv.imshow("Sofia", img)

capture = cv.VideoCapture("Videos/dog.mp4")
# set to 0 to capture from webcam
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)