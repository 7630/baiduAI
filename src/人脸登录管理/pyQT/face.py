#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 9:32
# @Author  : 廖荣森
# @File    : face.py

import  cv2

faceCascade = cv2.CascadeClassifier(r'D:\Users\12466\PycharmProjects\pythonProject\pyQT\facexml\haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)
OK = True
while OK:
    OK,img = cap.read() #mat  imread
    img = cv2.flip(img, 1)
    grap = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   # ret,binary = cv2.threshold(grap,0,255,cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)


    #图像检测
    faces = faceCascade.detectMultiScale(grap)
    print(faces)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0)) #BGR

    cv2.imshow("face", img)

    key = cv2.waitKey(1)
    if key == 27:
        OK = False
        break

cap.release()
cv2.destroyWindow()  #回收
