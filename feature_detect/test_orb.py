#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

import sys
import datetime

FLANN_INDEX_LSH    = 6
flann_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2      
                   
def match_images(frame,target):
    #创建检测器
    detector = cv2.ORB( nfeatures = 1000 )
    #创建匹配器
    matcher = cv2.FlannBasedMatcher(flann_params, {})
    
    #获取目标图的关键点和特征值，将来应只取一次（检测图每帧取一次）
    kp1, desc1 = detector.detectAndCompute(target, None)
    matcher.add([desc1])#将目标图的特征值加入匹配器供以后使用

    now=datetime.datetime.now()
    #获取检测图的关键点和特征值
    kp2, desc2 = detector.detectAndCompute(frame, None)
    print u'检测耗时     : ', datetime.datetime.now()-now, u'纳秒'    
    
    now=datetime.datetime.now()
    #计算匹配的特征点
    matches = matcher.knnMatch(desc2, k = 2)
    matches=[m[0] for m in matches if len(m) == 2 and m[0].distance < m[1].distance * 0.75]
    print u'匹配耗时     : ',datetime.datetime.now()-now, u'纳秒',u'找到',len(matches),u'个匹配点'
    
    now=datetime.datetime.now()
    #生成多边形
    p0=[kp1[m.trainIdx].pt for m in matches]
    p1 = [kp2[m.queryIdx].pt for m in matches]
    p0, p1 = np.float32((p0, p1))
    H, status = cv2.findHomography(p0, p1, cv2.RANSAC, 3.0)
    
    status = status.ravel() != 0
    p0, p1 = p0[status], p1[status]
    
    x0, y0, x1, y1 = 35,80,168,159
    quad = np.float32([[x0, y0], [x1, y0], [x1, y1], [x0, y1]])
    quad = cv2.perspectiveTransform(quad.reshape(1, -1, 2), H).reshape(-1, 2)
    print u'生成多边形耗时: ',datetime.datetime.now()-now, u'纳秒'
    
    return kp2,quad
    
def draw_quad(img,quad):
   cv2.polylines(img, [np.int32(quad)], True, (0, 0, 255), 3)    

#在图片上画出关键点
def draw_keypoints(img,keypoints):
    for kp in keypoints:
        x,y=kp.pt
        cv2.circle(img,(int(x),int(y)),5,(255,0,0))    

if __name__ == '__main__':
    #读入图片，假设是摄像头输出的一帧 
    frame = cv2.imread('f13.jpg')
    #目标图片
    target=cv2.imread('f11.jpg')
    
    kp,quad=match_images(frame,target)
    draw_keypoints(frame,kp)
    draw_quad(frame,quad)
    
    cv2.imshow('Image show', frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
