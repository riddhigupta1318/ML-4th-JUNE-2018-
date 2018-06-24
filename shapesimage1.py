#!/user/bin/python3 
import cv2 

#loading image 
img=cv2.imread("dogg.jpeg")
img3=cv2.imread("dog.jpeg")
img1=cv2.rectangle(img,(86,12),(175,86),(100,176,103),2)
img2=cv2.rectangle(img3,(143,94),(248,84),(100,176,103),-1)

#print height and width 
print(img.shape)



#to display that image 
cv2.imshow("dogg",img1)
cv2.imshow("doggie",img2)

#to save both images
cv2.imwrite("rect.jpeg",img1)
cv2.imwrite("face.jpeg",img2)

#image window holder activate 
#wait key will destroy by pressing q button 
cv2.waitKey(0)
cv2.destroyAllWindows()
