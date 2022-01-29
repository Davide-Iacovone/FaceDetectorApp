import cv2

cascade = cv2.CascadeClassifier('Cascade.xml')
cam = cv2.VideoCapture(0)
while True:
    ret,frame = cam.read()
    frame_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    
    face = cascade.detectMultiScale(frame_gray)

    for (x,y,w,h) in face:
        cv2.rectangle(frame_gray,(x,y),(x+w,y+h),(255,0,0),4)

    cv2.imshow('Video',frame_gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cam.release() 
cv2.destroyAllWindows()
