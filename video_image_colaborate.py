#!/usr/bin/python3
import cv2 

#loading image in a variable
load=cv2.imread('/home/leo/Downloads/11.jpg')
img=load[272:752,64:704]
#image dimension
print (img.shape)
#cv2.imshow('newwindowss',img)

#loading camera
cam=cv2.VideoCapture(0)
while  cam.isOpened() :
        #   real data of captured image stored in frame  
	#  processing and open status  of camera stored in status
	status,frame=cam.read()
	newimg=cv2.addWeighted(frame,0.8,img,0.5,0)
	#cv2.imshow('camera0',frame)
	cv2.imshow('camera0',newimg)
	print(newimg.shape)
	if  cv2.waitKey(1)  &  0xFF ==  ord('q')  :
		break
cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()
