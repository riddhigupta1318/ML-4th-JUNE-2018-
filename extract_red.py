#!/usr/bin/python3
import cv2
import time

#for image display
img1=cv2.imread('Redhat.jpeg')


time.sleep(5)
print(img1)

#extracting only red colour

red=cv2.inRange(img1,(0,0,0),(40,40,255))
cv2.imshow("original",img1)
cv2.imshow("only red",red)

#It will hold the image on the screen
cv2.waitKey(0)

#close the image
cv2.destroyAllWindows()








