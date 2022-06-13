#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 11:17
# @Author  : wx
# @File    : denglu.py
import  sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap
import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from register import *
# from codeRegister import *
# from  mul_camera import *
import winMa


class LoginWin(QWidget):
    #my_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.LoginUiInit()
        self.userpath = './registerInformation/users.txt'
        self.users = []
    def LoginUiInit(self):
        self.setWindowTitle("登录模块")
        self.setFixedSize(800,800)

        self.lab = QLabel(self)
        self.lab.setText("")
        self.lab.move(0,0)
        self.lab.resize(800,800)

        self.lab1 = QLabel(self)
        img_path = 'icon/3.jpg'  # 图片路径
        self.lab1.setStyleSheet("QLabel{\n"
                                "border-image:url(\"%s\");\n"

                                "}" % img_path)
        self.lab1.move(0, 0)
        self.lab1.resize(800, 800)


        self.btn = QPushButton(self)
        self.btn.setToolTip("登录")
        #self.btn.setText("登录")
        self.btn.setMaximumSize(60, 60)
        self.btn.setMinimumSize(60,60)
        img_path = 'icon/denglu.png'  # 图片路径
        self.btn.setStyleSheet("QPushButton{\n"
                               "border-image:url(\"%s\");\n"
                               "}" % img_path)
        self.btn.move(275,490)

        self.btn2 = QPushButton(self)
        self.btn2.setToolTip("注册")
        #self.btn2.setText("注册")
        self.btn2.setMaximumSize(50, 50)
        self.btn2.setMinimumSize(50, 50)
        img_path = 'icon/zhuce.png'  # 图片路径
        self.btn2.setStyleSheet("QPushButton{\n"
                               "border-image:url(\"%s\");\n"
                               "}" % img_path)
        self.btn2.move(400,490)

        self.face_btn = QPushButton(self)
        self.face_btn.setToolTip("人脸登录")
        #self.face_btn.setText("人脸登录")
        self.face_btn.setMaximumSize(50, 50)
        self.face_btn.setMinimumSize(50, 50)
        img_path = 'icon/renliandenglu.png'  # 图片路径
        self.face_btn.setStyleSheet("QPushButton{\n"
                               "border-image:url(\"%s\");\n"
                               "}" % img_path)
        self.face_btn.move(275, 600)


        self.face_btn2 = QPushButton(self)
        self.face_btn2.setToolTip("人脸注册")
        #self.face_btn2.setText("人脸注册")
        self.face_btn2.setMaximumSize(50, 50)
        self.face_btn2.setMinimumSize(50, 50)
        img_path = 'icon/renlianzhuce.png'  # 图片路径
        self.face_btn2.setStyleSheet("QPushButton{\n"
                               "border-image:url(\"%s\");\n"
                               "}" % img_path)
        self.face_btn2.move(400, 600)

        self.linedit = QLineEdit(self)
        self.linedit.setStyleSheet(
            "QLineEdit{font-size:35px;}")
        rx = QRegExp("^[0-9A-Za-z]{8,18}$")
        self.linedit.setValidator(QRegExpValidator(rx, self))
        self.linedit.setFixedSize(400,50)
        self.linedit.move(250,330)

        self.linedit2 = QLineEdit(self)
        self.linedit2.setStyleSheet(
            "QLineEdit{font-size:35px;}")
        self.linedit2.setFixedSize(400,50)
        self.linedit2.move(250,420)
        self.linedit2.setEchoMode(QLineEdit.Password)

        self.lableEdit = QLabel(self)
        self.lableEdit.setText("账号")
        self.lableEdit.setStyleSheet(
            "QLabel{color:rgb(0,0,127,255);font-size:35px;font-weight:normal;font-family:Arial;}")
        self.lableEdit.setFixedSize(70,50)
        self.lableEdit.move(150,330)

        self.lableEdit1 = QLabel(self)
        self.lableEdit1.setText("密码")
        self.lableEdit1.setStyleSheet(
            "QLabel{color:rgb(0,0,127,255);font-size:35px;font-weight:normal;font-family:Arial;}")
        self.lableEdit1.setFixedSize(70,50)
        self.lableEdit1.move(150,420)

        self.face_btn2.clicked.connect(self.facebtn2_slot)
        self.face_btn.clicked.connect(self.faceLogin)
        self.btn2.clicked.connect(self.codereg)
        self.btn.clicked.connect(self.LoginCam)
    def facebtn2_slot(self):
        winMa.reg.show()
        self.close()
        pass
    def faceLogin(self):
        winMa.reg.show()
        self.close()
        pass
    def codereg(self):
        winMa.code.show()
        self.close()
        pass
    def LoginCam(self):
        users = self.file_read(self.userpath)
        name = self.linedit.text()
        pwd = self.linedit2.text()
        self.userFlag = False
        print(users)
        if name:
            for i in range(0, len(users)):
                if name == list(users[i].values())[0]:
                    self.userFlag = True
                    break
            if self.userFlag:
                if pwd:
                    if pwd == list(users[i].values())[1]:
                        winMa.cam.show()
                        self.close()
                    else:
                        QMessageBox.warning(self, "警告", "密码错误")
                else:
                    QMessageBox.warning(self, "警告", "还未输入密码")
            else:
                QMessageBox.warning(self, "警告", "用户名不存在")
        else:
            QMessageBox.warning(self, "警告", "用户名不能为空")
        print(self.userFlag)
        pass

    def file_writer(self, file_path, user):
        with open(file_path, mode="a+") as file:
            file.write(user["name"] + "," + user["pwd"] + "\n")
        pass

    def file_read(self, file_path):
        with open(file_path, mode="r") as file:
            for line in file.readlines():
                line = line.strip()
                name, pwd = line.split(",")
                newuserdict = {"name": name, "pwd": pwd}
                self.users.append(newuserdict)
            return self.users
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginWin()
    #win.reg = VideoRegister()
    # code = Register()
    # cam = CameraVideo()
    win.show()
    sys.exit(app.exec_())