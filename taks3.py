from tkinter import font
import cv2

def show_image(cam, face_detection=cv2.CascadeClassifier('Cascade.xml'),
                smile_detection=cv2.CascadeClassifier('haarcascade_smile.xml')):
    
    while True:
        ret,frame = cam.read()
        
        frame_gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
        face = face_detection.detectMultiScale(frame_gray)

        for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(251,72,196),4)

            smile_place = frame_gray[y:y+h,x:x+w]
            smile_color = frame[y:y+h,x:x+w]

            smile = smile_detection.detectMultiScale(smile_place,1.7,22)
            if(len(smile)):
                cv2.putText(frame,'Smiling',(x,y-12),
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,
                                color=(200,255,155))

                for (sx,sy,sw,sh) in smile:
                    cv2.rectangle(smile_color,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
            
            else:
                cv2.putText(frame,'Not Smiling',(x,y-12),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,
                        color=(200,255,155))
            

        cv2.imshow('Video',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

cam = cv2.VideoCapture(0)

show_image(cam)

cam.release() 
cv2.destroyAllWindows()
