#!/usr/bin/python3

import cv2

# capture camera start
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    #converting to HSV
    hsvimg=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   
    # MASKING IMAGE for green color
    imgmask=cv2.inRange(hsvimg,(40,50,50),(80,255,255))
    # for blue color
   
    # bitwise mask and original frame 
    redpart=cv2.bitwise_and(frame,frame,mask=imgmask)
    # showing images
    cv2.imshow('original',frame)
    #cv2.imshow('mask',imgmask)
    cv2.imshow('red',redpart)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
