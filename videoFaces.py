import cv2

cascade = cv2.CascadeClassifier("Cascade.xml")
video = cv2.VideoCapture(0)

while(True):
    tmp, image = video.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray_image)

    for (x, y, w, h) in face:
        cv2.rectangle(image, (x,y), (x+w, y+h), (180, 105, 255), 6)
    
    cv2.imshow("Video", image)
    #cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()