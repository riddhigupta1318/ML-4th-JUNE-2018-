#!user/bin/python3
import cv2
import time

cap=cv2.VideoCapture(0)

while cap.isOpened():
	#taking frame 
	status,frame=cap.read()

	#extracting only red colour 
	onlyred=cv2.inRange(frame,(0,0,0),(40,40,255))
	cv2.imshow("camera1",onlyred)
	if  cv2.waitKey(1)  &  0xFF == ord('q'):
		break 
       

cv2.destroyAllWindows()
cap.release()



