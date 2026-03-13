import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
print(img.shape)

img[:]=25,205,30 #BGR

## Creating a Line

cv2.line(img,(0,0),(300,400),(0,0,255),9)

## Creating a Rectangle

cv2.rectangle(img,(0,0),(260,360),(0,0,245),5)

## Creating a Circle

cv2.circle(img,(260,360),60,(0,0,245),5)

## Put Text

cv2.putText(img,"Computer Vision",(200,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

cv2.imshow("Images",img)
cv2.waitKey(0)