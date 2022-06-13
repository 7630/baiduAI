#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 10:52
# @Author  : 廖荣森
# @File    : food.py
# encoding:utf-8

import requests
import base64


# client_id 为官网获取的AK， client_secret 为官网获取的SK
def get_access_token(client_id,client_secret):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id,client_secret)
    response = requests.get(host)
    if response:
        print(response.json())
        return  response.json()['access_token']
    pass


'''
菜品识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
# 二进制方式打开图片文件
f = open('./img4.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img,"top_num":5}
#令牌
access_token = get_access_token(client_id="fldXYAM1tIDBItLLYBmpGAre",client_secret="T6d3x1XcvtSWMQ3RGVr82sNZ5oTGYCju")
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json()['result'][0]['name'])