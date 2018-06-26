#!user/bin/python3
import cv2 
import random

face_data=cv2.CascadeClassifier('face.xml')
cap=cv2.VideoCapture(0)
while cap.isOpened():
	status,img=cap.read()
	grayimage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_data.detectMultiScale(grayimage,1.15,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray=grayimage[y:y+h,x:x+w]
		roi_color=img[y:y+h,x:x+w]

	#showing current image
	cv2.imshow("current image",img)
	
	#to generate random no.
	x=random.random()
	y=str(x)[5:8]

	cv2.imwrite('adhoc'+y+'.jpg',img)

	if cv2.waitKey(1) &  0xFF  ==  ord('q'):
		break

#to end
cv2.DestroyAllWindows()
cap.release()


