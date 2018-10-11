import cv2,os
import numpy as np
import sqlite3
from PIL import Image 
import pickle
conn = sqlite3.connect('attendance.db')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(Null,"Cat",(x,y-10),font,0.55,(0,255,0),1)
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(0,225,0),3)
        if(nbr_predicted==7):
             nbr_predicted='Obama'
        elif(nbr_predicted==2):
             nbr_predicted='Anirban'
        elif(nbr_predicted==8):
             nbr_predicted='Mandeep'
        elif(nbr_predicted==1543136):
             nbr_predicted='Simran Kanda'
         #    cursor = conn.execute("SELECT Roll from data")
          #   for i in cursor:
           #      print i
            # if (nbr_predicted,) in  cursor:
             #   print("oyo")
             #conn.execute("INSERT INTO data (Name,Roll)\
              #  VALUES ('Simran',156)");
             #cursor = conn.execute("SELECT Name,Roll from data")
        #for row in cursor:
         #        print "Name=", row[0]
          #       print "Roll=", row[1]
           
        #if(nbr_predicted,) in cursor:
         #   print "present"
        #for i in cursor:
        # print cursor
        #elif (nbr_predicted,) not in  cursor:
         #        print("absent")
        elif(nbr_predicted==67): 
             nbr_predicted='Sandeep'
          
        elif(nbr_predicted==1):
             nbr_predicted='Harry Potter'
        elif(nbr_predicted==1452126):
             nbr_predicted='Ritesh Kumar Singh'
        elif(nbr_predicted==1542260):
             nbr_predicted='Nikita Digra'
        elif(nbr_predicted==1543157):
             nbr_predicted='Tanu'
        elif(nbr_predicted==1542520):
             nbr_predicted='Rabia Mahajan'
        elif(nbr_predicted==1543131):
             nbr_predicted='Shivani Sharma'
        elif(nbr_predicted==1544778):
             nbr_predicted='Ramandeep Kaur'
        elif(nbr_predicted==1543821):
             nbr_predicted='Deepak Singh'
        elif(nbr_predicted==1544054):
             nbr_predicted='Jyoti Sharma'
        elif(nbr_predicted==1542317):
             nbr_predicted='Pankaj Bawa'
        elif(nbr_predicted==1543072):
             nbr_predicted='Rasbihari Sharma'
             
            
                         
        #cv2.cv.PutText(cv2.cv.fromarray(im),str(nbr_predicted)+"--"+str(conf), (x,y+h),cv2.cv.FONT_HERSHEY_PLAIN, 255) #Draw the text
        cv2.putText(im,str(nbr_predicted), (x,y-55), font, 1, (225,255,225), 2)
        cv2.imshow('im',im)
        print(nbr_predicted)
        cv2.waitKey(10)
        






