from cv2 import imread, imshow,waitKey,destroyAllWindows
from cv2 import cvtColor,COLOR_RGB2GRAY,rectangle
from cv2 import CascadeClassifier

cascade = CascadeClassifier('Cascade.xml')
photo = imread('face1.jpg')
photo_gray = cvtColor(photo,COLOR_RGB2GRAY)

face = cascade.detectMultiScale(photo_gray,1.1,3)
"""
Narysowanie prostokątu na jednej twarzy
rectangle(photo_gray,(face[0][0],face[0][1]),(face[0][0]+face[0][2],face[0][1]+face[0][3]),(255,0,0),3)

"""

for (x,y,w,h) in face:
    rectangle(photo_gray,(x,y),(x+w,y+h),(255,0,0),4)

imshow('GRAY',photo_gray)
waitKey(0)
destroyAllWindows()