#!/usr/bin/python3
import cv2
capture=cv2.VideoCapture(0)

#for opening camera
if capture.isOpened():
   print("camera is ready to take snap")

else:
   print("check your camera driver with OS")

#frame is current camera data
status,frame=capture.read()
cv2.imshow("frame",frame)
cv2.waitKey(0)
capture.release()


