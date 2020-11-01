from cv2 import cv2
import time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21), 0)
    
    if not first_frame:
        first_frame = gray
        continue
    
    
    cv2.imshow("Capturing", gray)
    
    key = cv2.waitKey(1)
    print(gray)
     
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()