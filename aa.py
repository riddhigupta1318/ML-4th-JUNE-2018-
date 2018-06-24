#!/user/bin/python3 
import cv2 

#loading image 
img=cv2.imread("dog.jpeg")
img1=cv2.imread("dogg.jpeg")
img2=cv2.imread("dog1.jpeg",0)

#print height and width 
print(img.shape)
print(img1.shape)
print(img2.shape)


#to display that image 
cv2.imshow("dog",img)
cv2.imshow("dogg",img1)
cv2.imshow("dog1",img2)

#for saving image
cv2.imwrite("new.jpeg",img2)

#image window holder activate 
#wait key will destroy by pressing q button 
cv2.waitKey(0)
cv2.destroyAllWindows()



