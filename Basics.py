import cv2

##Reading images

img=cv2.imread("Resources/Screenshot 2026-03-12 225422.png")

print(img)
print(img.shape)
cv2.imshow("Batman",img)
cv2.waitKey(0)

##Reading videos

cap=cv2.VideoCapture("Resources/6994190_Cyborg_Generative_Ai_3840x2160.mp4")

print(cap)

while True:
    success,frame=cap.read()
    print(frame.shape)
    cv2.imshow("Output",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
     break 
