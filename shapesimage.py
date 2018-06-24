#!/user/bin/python3 
import cv2 

#loading image 
img=cv2.imread("dog.jpeg")
img1=cv2.line(img,(0,0),(200,114),(110,176,123),2)

#print height and width 
print(img.shape)



#to display that image 
cv2.imshow("dogg",img1)


#image window holder activate 
#wait key will destroy by pressing q button 
cv2.waitKey(0)
cv2.destroyAllWindows()
