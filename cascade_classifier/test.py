#!/usr/bin/python 
# -*- coding: utf-8 -*-

import cv2
import datetime

img = cv2.imread("p1.jpg")

minisize = (img.shape[1]/4,img.shape[0]/4)

hc = cv2.CascadeClassifier("lbpcascade_frontalface.xml")
img=cv2.resize(img, minisize)

now=datetime.datetime.now()
faces = hc.detectMultiScale(img)
print datetime.datetime.now()-now

for face in faces:
     cv2.rectangle(img, (face[0], face[1]), (face[0] + face[2], face[0] + face[3]), (255, 0, 0), 3)
     
cv2.imshow('face', img)

if cv2.waitKey(15000) == 27:
    cv2.destroyWindow('face')

#cv2.imwrite("face.png", img)