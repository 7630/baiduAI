#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 15:54
# @Author  : 廖荣森
# @File    : faceCompare.py

# encoding:utf-8
import json
import requests
import base64
import cv2

def get_access_token(client_id,client_secret):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id,client_secret)
    response = requests.get(host)
    if response:
        print(response.json())
        return  response.json()['access_token']
    pass

f1=open('4.jpg','rb')
img1 = str(base64.b64encode(f1.read()),'utf-8')
#print("img1",img1)
f2=open('5.jpg','rb')
img2 = str(base64.b64encode(f2.read()),'utf-8')
# print("img2",img2)
'''
人脸对比
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"

#
params = json.dumps([
    {
        "image": img1,
        "image_type": "BASE64",
        "face_type": "LIVE",
        "quality_control": "LOW",
    },
    {
        "image":img2,
        "image_type": "BASE64",
        "face_type": "LIVE",
        "quality_control": "LOW",
    }
])

#params='([{"image":"' + img1 + '","image_type": "BASE64"},{"image": "' + img2 + '","image_type": "BASE64"}])'
params = eval(params)

access_token = get_access_token("6m45tPZplBxAuPjbPGOeqyxP","6SkTelgcOKBK6UTgh3cOQUwwhvVWnvBQ")
request_url = request_url + "?access_token=" + access_token
# print(request_url)
headers = {'content-type': 'application/json'}
# print(params)
response = requests.post(request_url, json=params, headers=headers)

if response:
    #print (response.json())
    print(response.json()['result']['score'])
    if response.json()['result']['score']>95:
        print("same")