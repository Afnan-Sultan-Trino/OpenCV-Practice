import cv2
import numpy as np

width,height=250,300

img=cv2.imread("Resources/WhatsApp Image 2026-03-12 at 11.08.35 PM.jpeg")

pts1=np.float32([[559,58],[1010,227],[332,615],[752,833]]) ## specific part to co-ordinate using "Paint"
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]]) ## always same formula for window

matrix=cv2.getPerspectiveTransform(pts1,pts2)
img_out=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Cards',img)
cv2.imshow('Cards Warp',img_out)

cv2.imshow('Cards',img)
cv2.waitKey(0)

