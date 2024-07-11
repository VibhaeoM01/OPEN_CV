import cv2 as cv



def rescaleFrame(frame, scale=0.75):
    #works for images,video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dim=(width,height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def changeRes(width,height):
    #Only work for live video
    capture.set(3,width)
    capture.set(4,height) 





#READS AND RESIZES THE IMAGE
img=cv.imread("Resources\Photos\cat.jpg")
cv.imshow('cat',img)
resized_image=rescaleFrame(img)



#READS/CAPTURE THE VIDEO AND RESIZE IT
capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame=capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
   

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)

