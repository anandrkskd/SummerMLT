#!/usr/bin/python3

import cv2,numpy
#empty list to store the data of each images
list_of_pics=[]


#reading and appending different image data
img=cv2.imread('/home/leo/Downloads/pics/1.jpg')
list_of_pics.append(img)
img=cv2.imread('/home/leo/Downloads/pics/2.jpg')
list_of_pics.append(img)
#img=cv2.imread('/home/leo/Downloads/pics/red.jpg')
#list_of_pics.append(img)
img=cv2.imread('/home/leo/Downloads/pics/green.jpg')
list_of_pics.append(img)


#writes the image array data into the file
f=open('array_of_images.txt',"+w")
f.write(str(list_of_pics))
f.close()


#show all the images contained in the array
'''
i=0
try:
	while i<4:
		img=list_of_pics[i]
		cv2.imshow('arr',img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		i=i+1
except:
	print("THANKS")
'''
