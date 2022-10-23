import cv2
from datetime import datetime

def get_time():
    return datetime.now().strftime("%H:%M:%S")

webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    status, img = webcam.read()
    if not status:
        print("Camera not working")
        break
    h,w,_ = img.shape
    img = cv2.resize(img, (w*2, h*2))
    
    msg = "Camera 0: Live Feed"
    pos = (10, 30)
    font = cv2.FONT_ITALIC
    color = (0, 255, 0) # BGR
    cv2.putText(img, msg, pos, font, 1, color, 2)
    cv2.putText(img, get_time(), (10, 60), font, .5, color, 2)

    cv2.imshow("Webcam", img)
    # press esc to exit 
    if cv2.waitKey(5) == 27:
        break
webcam.release()
cv2.destroyAllWindows()