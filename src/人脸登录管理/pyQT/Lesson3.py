#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 9:27
# @Author  : 廖荣森
# @File    : Lesson3.py
from  PyQt5.QtCore import  *
from  PyQt5.QtWidgets import  *
from  PyQt5.QtGui import  *
import  sys
from  loginWindet import *
from facewin import  *

if __name__ ==  '__main__':
    app = QApplication(sys.argv)
    LoginWin = LoginWin()
    LoginWin.show()
    # LoginWin = QWidget() #空白窗口界面
    # LoginWin.setWindowTitle("登录界面")
    # LoginWin.setFixedSize(600,600)
    # LoginWin.setStyleSheet("color:red")
    # LoginWin.show()
    sys.exit(app.exec_())