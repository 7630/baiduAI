#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 15:14
# @Author  : 廖荣森
# @File    : faceAI.py

# encoding:utf-8

import requests
import base64
import cv2
'''
人脸检测与属性分析
'''
def get_access_token(client_id,client_secret):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id,client_secret)
    response = requests.get(host)
    if response:
        print(response.json())
        return  response.json()['access_token']
    pass

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

filename = './xuzijun.jpg'
img = cv2.imread(filename)

f = open(filename,'rb')
img_test = base64.b64encode(f.read())

params = {"image":''+str(img_test,'utf-8')+'',"image_type":'face_field',"face_field":"faceshape,facetype"}

access_token = get_access_token(client_id="6m45tPZplBxAuPjbPGOeqyxP",client_secret="6SkTelgcOKBK6UTgh3cOQUwwhvVWnvBQ")
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())


