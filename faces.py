import cv2

cascade = cv2.CascadeClassifier("LeftEyeCascade.xml")
image1 = cv2.imread("face1.jpg")
gray_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

#cv2.imshow("image", gray_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

face = cascade.detectMultiScale(gray_image)
(x, y, w, h) = face[0]
cv2.rectangle(image1, (x,y), (x+w, y+h), (0, 255, 0), 10)

cv2.imshow("image", image1)
cv2.waitKey(0)