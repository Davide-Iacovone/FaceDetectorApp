import cv2

cascade = cv2.CascadeClassifier("Cascade.xml")
left_eye_cascade = cv2.CascadeClassifier("LeftEyeCascade.xml")
video = cv2.VideoCapture(0)

while True:
    tmp, image = video.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray_image)

    for (xF, yF, wF, hF) in face:
        eye = left_eye_cascade.detectMultiScale(gray_image)
        eyes =[]
        for (x, y, w, h) in eye:
            eyes.append(x)
        cv2.rectangle(image, (min(eyes),y), (min(eyes)+w, y+h), (180, 105, 255), 4)
    
    cv2.imshow("Video", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()