#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import cv2

import sys
import datetime

from pprint import pprint

FLANN_INDEX_LSH    = 6
flann_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2
        
def dump(obj):
  for attr in dir(obj):
    print "obj.%s = %s" % (attr, getattr(obj, attr))        
                   
def match_images(img):
    detector = cv2.ORB( nfeatures = 1000 )
    matcher = cv2.FlannBasedMatcher(flann_params, {})

    now=datetime.datetime.now()
    kp, desc = detector.detectAndCompute(img, None)
    print u'检测耗时: ', datetime.datetime.now()-now, u'纳秒'    
    
    return kp

def draw_keypoints(img,keypoints):
    for kp in keypoints:
        x,y=kp.pt
        cv2.circle(img,(int(x),int(y)),2,(0,255,255))    

if __name__ == '__main__': 
    frame = cv2.imread('f1.jpg')
    
    kp=match_images(frame)
    draw_keypoints(frame,kp)
    
    cv2.imshow('Image show', frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
