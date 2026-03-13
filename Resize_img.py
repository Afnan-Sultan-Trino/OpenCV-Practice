import cv2

## Resizing images

# img=cv2.imread('Resources/WhatsApp Image 2026-03-12 at 11.08.36 PM.jpeg')
# print(img.shape)

# resized_img=cv2.resize(img,(900,100)) ##resize func. to resize any dimension
# print(resized_img.shape)

# cv2.imshow("Actual Image",img)
# cv2.imshow("Resize Image",resized_img)
# cv2.waitKey(0)

## Croping Image

img=cv2.imread('Resources/WhatsApp Image 2026-03-12 at 11.08.36 PM.jpeg')
print(img.shape)

crop_img=img[0:200,200:600]
print(crop_img.shape)

cv2.imshow("Actual Image",img)
cv2.imshow("Crop Image",crop_img)
cv2.waitKey(0)
