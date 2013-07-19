#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

#可命名的元组？
#from collections import namedtuple

#Person=namedtuple('Person','name age gender')
#person=Person('zhangsan',30,'male')
#print 'person: ', person.name

#person=('zhangsan',30,'male')
#name,age,gender=person
#print name,'-',age

#函数的关键参数
#def my_test(a1,a2=2,a3=''):
#    print a3

#my_test('a1',a3='a3')

#[m[0] for m in matches if len(m) == 2 and m[0].distance < m[1].distance * 0.75]
#matches=[[1,2],[2,3]]
#for m in matches:
#    if len(m)==2:
#        print m[0]
#print [m[0] for m in matches if len(m)==2 and m[0]==1]

img=cv2.imread('f1.jpg',0)
h,w=img.shape[:2]
print 'load img ok, w:',w,', h: ',h


