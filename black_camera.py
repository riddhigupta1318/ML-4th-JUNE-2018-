#!/usr/bin/python3
import cv2
import random
capture=cv2.VideoCapture(0)
while  capture.isOpened() :
	print("camera is working")

	status,frame=capture.read()
	bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow("camera1",frame)
	cv2.imshow("camera2",bwimg)

	#to generate random no.
	x=random.random()
	y=str(x)[5:8]

	cv2.imwrite('adhoc'+y+'.jpg',frame)

	if cv2.waitKey(1) & 0XFF == ord('q'):
		break

#to close window 
cv2.destroyWindow("camera1")
cv2.destroyWindow("camera2 ")
capture.release()


