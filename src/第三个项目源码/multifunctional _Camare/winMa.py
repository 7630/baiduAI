#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 9:46
# @Author  : 廖荣森
# @File    : winMa.py


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap
# from PyQt5.QtWidgets import *
from codeRegister import *
from denglu import *
from mul_camera import *
from register import *
from PyQt5.QtCore import pyqtSignal
import cv2
import numpy as np
import  sys


# if __name__ == "__main__":
app = QApplication(sys.argv)
code = Register()      #账号密码注册界面
reg = VideoRegister()  #人脸注册界面
login = LoginWin()     #登录界面
cam = CameraVideo()    #功能界面
#reg.show()


