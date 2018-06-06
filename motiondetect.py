#!/usr/bin/python3

import cv2 
import time
import numpy

cap=cv2.VideoCapture(0) 
time.sleep(1)
tp1=cap.read()[1]

time.sleep(1)
tp2=cap.read()[1]

time.sleep(1)
tp3=cap.read()[1]

diff1=cv2.absdiff(tp1,tp2)
diff2=cv2.absdiff(tp2,tp3)
fd=cv2.bitwise_and(diff1,diff2)
#print(fd)

cv2.imshow('diff1',diff1)
cv2.imshow('diff2',diff2)
cv2.imshow('diff',fd)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
