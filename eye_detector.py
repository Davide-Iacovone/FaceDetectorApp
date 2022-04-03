print("ok")
import cv2

cascade = cv2.CascadeClassifier("Cascade.xml")
left_eye_cascade = cv2.CascadeClassifier("LeftEyeCascade.xml")
video = cv2.VideoCapture(0)

while True:
    tmp, image = video.read()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = cascade.detectMultiScale(gray_image)

    for (xF, yF, wF, hF) in face:
        detected_face = image[yF:yF + hF, xF:xF + wF]
        eye = left_eye_cascade.detectMultiScale(detected_face)
        eyes =[]
        for (x, y, w, h) in eye:
            eyes.append(x)
        if len(eyes) > 0:
            cv2.rectangle(detected_face, (max(eyes),y), (max(eyes)+w, y+h), (180, 105, 255), 4)
    
    cv2.imshow("Video", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()