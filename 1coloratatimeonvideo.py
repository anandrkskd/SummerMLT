#!/usr/bin/python3


import cv2

#  loading image
#img=cv2.imread('/home/leo/Downloads/red.jpg')

#print(img.shape)

#  only picking  red color range
#  starting  camera  
cap=cv2.VideoCapture(0)
#  checking for  web  cam 
while cap.isOpened():
	# true ,false , image frame 
	status,img=cap.read()
        #                           starting color, end color range
	only_red=cv2.inRange(img,(0,0,20),(20,20,255))
	if 255 in  only_red:
		print("yes")
		imgnew=cv2.imread('/home/leo/Downloads/1.jpg')
		cv2.imshow('went',imgnew)
		cv2.waitKey(1000)
		break
	cv2.imshow('window_red',only_red)
	if  cv2.waitKey(1) & 0xFF ==  ord('q') :
		break
#cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()

