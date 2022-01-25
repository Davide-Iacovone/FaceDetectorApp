from cv2 import CascadeClassifier, imread, cvtColor, COLOR_BGR2GRAY, rectangle, imshow, waitKey

classifier = CascadeClassifier('Cascade.xml')
image = imread('image.jpg')
greyScaleImage = cvtColor(image, COLOR_BGR2GRAY)
faces = classifier.detectMultiScale(greyScaleImage, 2.1, 2)

for (x, y, w, h) in faces:
    rectangle(image, (x-2, y-2), (x + w, y + h), (0, 0, 255), 2)
imshow('image', image)
waitKey()

