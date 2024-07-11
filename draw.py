import cv2 as cv
import numpy as np



#creating a blank image           unsigned 8 bit integers  means value in array can range from (0,255)
blank=np.zeros((500,500,3), dtype='uint8')
#np.zeros(): This is a function from the NumPy library that creates a new array filled with zeros.

blank1=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)



# 1. Paint the image a certain colour

        #R ,G, B
# blank[:]=0,255,0  # for ex lets take green  
# cv.imshow("Green Image",blank)

# blank1[300:400, 200:300] = 0,255,0
# cv.imshow("Green Block",blank1)




# # 2. Draw a rectangle 
# cv.rectangle(blank,(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3)   #TO FILL RECTANGLE thickness=-1 OR thickness=cv.FILLED
# cv.imshow('Rectangle',blank)  

# # (blank.shape[1]//2, blank.shape[0]//2) Can be used instead of points
# #blank.shape[1] full width of blank ,blank.shape[0] full width of blank




# #3. Draw a circle
# cv.circle(blank,(150,150), 30, (255,0,0) ,thickness=-1) #TO FILL RECTANGLE thickness=-1 OR thickness=cv.FILLED
# cv.imshow('Circle', blank)




#4. Draw a line
cv.line(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,0,255),thickness=5)
cv.imshow('Line',blank)



#Write text on image
cv.putText(blank,'Hello, I am Vibhaeo',(0,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('Text',blank)











cv.waitKey(0)


