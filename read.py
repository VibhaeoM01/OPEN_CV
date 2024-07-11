import cv2 as cv


#Reading videos in open cv

img=cv.imread('Resources\Photos\cat_large.jpg')

#display image
cv.imshow('Cat', img )




#Reading videos in open cv

# ##     capture=cv.VideoCapture(0,1,2) #if we are connected to camera to capture video
capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()

    cv.imshow('Video', frame)

   

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)