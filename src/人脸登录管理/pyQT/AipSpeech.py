#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 9:50
# @Author  : 廖荣森
# @File    : AipSpeech.py

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '24472339'
API_KEY = 'DaCaN5nSNI8CYtUO2AWeGOBq'
SECRET_KEY = 'GFiFw1pbhpt9j2yHD3Qt0MCNX7GZ5DNh'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
ret = client.asr(get_file_content('16k.pcm'), 'pcm', 16000, {
    'dev_pid': 1537,
})
print(ret)
print(ret["result"])