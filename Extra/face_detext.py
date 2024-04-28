import cv2 as cv
from rescale import rescaleFrame

# answer = input("Pick which image you would like to use")
# if (answer == 1):
#     img = cv.imread("Photos/sofia.jpg")
# elif(answer == 2):
img2 = cv.imread("Photos/sofia2.jpg")
# elif(answer == 3):
#     img = cv.imread("Photos/enj.jpg")
# else:
#     img = cv.imread("Photos/sofia.jpg")

# img = cv.imread("Photos/sofia.jpg")
# img2 = rescaleFrame(img, scale=.2)

cv.imshow("Sofia Resized", img2)

gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Sofia", gray)

haar_cascade = cv.CascadeClassifier("C:\Programming\OpenCV\haar_face.xml")

# in a busy picture, increase minNeighbors to detect fewer cascades
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=9)
print(f"Number of faces found = {len(faces_rect)}" )

for (x,y,w,h) in faces_rect:
    cv.rectangle(img2, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow("Detected Faces", img2)

cv.waitKey(0)