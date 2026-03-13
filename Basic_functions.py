
import cv2

## Basic functions in OpenCV


###1. Convert color image to Grey-Scale image :

img=cv2.imread("Resources/Screenshot 2026-03-12 225422.png")
cv2.imshow("Original Image",img)

img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray-Scale Image",img_grey)

print(img.shape)
print(img_grey.shape)
cv2.waitKey(0)


# ### 2. Convert image to Blur image : (at first, we have to make it grey-scale image,then blur iamge)

img=cv2.imread("Resources/Screenshot 2026-03-12 225422.png")
cv2.imshow("Original Image",img)

img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray-Scale Image",img_grey)

img_blur=cv2.GaussianBlur(img_grey,(7,7),0) ## GaussianBlur function to convert it blur
cv2.imshow("Blur Image",img_blur)

print(img.shape)
print(img_grey.shape)
print(img_blur.shape)
cv2.waitKey(0)


### 3. Convert image to Canny image/edge detection : 

img=cv2.imread("Resources/Screenshot 2026-03-12 225422.png")
cv2.imshow("Original Image",img)

img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray-Scale Image",img_grey)

img_blur=cv2.GaussianBlur(img_grey,(7,7),0) 
cv2.imshow("Blur Image",img_blur)

img_canny=cv2.Canny(img_blur,100,100) ##Canny function to convert it
cv2.imshow("Canny Image",img_canny)

print(img.shape)
print(img_grey.shape)
print(img_blur.shape)
print(img_canny.shape)
cv2.waitKey(0)