#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 10:05
# @Author  : 廖荣森
# @File    : loginWindet.py
#from  PyQt5.QtWidgets import  QApplication,QWidget,QPushButton,QLineEdit,QTextEdit,QLabel,QMouseEventTransition,QFileDialog,QComboBox
import  sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap
import cv2
import numpy as np


class LoginWin(QWidget):
    my_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.LoginUiInit()
        #self.my_signal.connect(self.ChangeText)

    def LoginUiInit(self):
        self.setWindowTitle("登录模块")
        self.setFixedSize(800,800)

        self.lab = QLabel(self)
        self.lab.setText("")
        self.lab.move(0,0)
        self.lab.resize(800,800)


        btn = QPushButton(self)
        btn.setText("登录")
        btn.move(275,480)
        btn2 = QPushButton(self)
        btn2.setText("注册")
        btn2.move(400,480)


#        btnsure.pressed.connect(self,ImageChange)

        linedit = QLineEdit(self)
        linedit.setFixedSize(300,50)
        linedit.move(250,330)
        linedit2 = QLineEdit(self)
        linedit2.setFixedSize(300,50)
        linedit2.move(250,420)

        lableEdit = QLabel(self)
        lableEdit.setText("账号")
        lableEdit.setFixedSize(60,50)
        lableEdit.move(180,330)

        lableEdit1 = QLabel(self)
        lableEdit1.setText("密码")
        lableEdit1.setFixedSize(60,50)
        lableEdit1.move(180,420)

        self.btn1 = QPushButton(self)
        self.btn1.move(600, 400)
        self.btn1.setText("打开")
        #  self.btn1.pressed.connect(self,OpenFile)
        self.btn1.pressed.connect(self.OpenFile)

        # self.btnsure = QPushButton(self)
        # self.btnsure.move(600, 700)
        # self.btnsure.setText("确认")
        # self.btnsure.pressed.connect(self,ImageChange)

        self.combox = QComboBox(self)
        self.combox.move(600,600)
        self.combox.addItems(['x轴翻转','y轴翻转','原点对称','图片取1/4','截取'])
        #btn.my_signal.connect()
        btn.pressed.connect(self.ChangeText)
        btn2.pressed.connect(self.ChangeText1)

        self.btn1 = QPushButton(self)
        self.btn1.move(600, 400)
        self.btn1.setText("打开")
        #  self.btn1.pressed.connect(self,OpenFile)
        self.btn1.pressed.connect(self.OpenFile)

        self.btnsure = QPushButton(self)
        self.btnsure.move(600, 700)
        self.btnsure.setText("确认")
        self.btnsure.pressed.connect(self.ImageChange)

    def ChangeText(self):
        print("登录")
    def ChangeText1(self):
        print("注册")

    def mousePressEvent(self, QMouseEvent):
        self.my_signal.emit()

    def OpenFile(self):
        self.imagepath = QFileDialog.getOpenFileName(None,"选择图片","./","All File(*);;")
        #self.lab.setStyleSheet("border-image:url("+self.imagepath[0] +")")
        self.imageshow()

    def ImageChange(self):
        #获取下拉框 文本信息
        print(self.combox.currentText())
        if self.combox.currentText() == 'x轴翻转':
            print(self.imagepath[0])
            img = cv2.imread(self.imagepath[0])
            img_x = img[::-1,:,:]
            matimg = img_x.astype(np.uint8)#bgr
            rgbimg = QImage(matimg.data,matimg.shape[1],matimg.shape[0],matimg.shape[1]*3,QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(),self.lab.height()))
            pass
        elif self.combox.currentText() == 'y轴翻转':
            img = cv2.imread(self.imagepath[0])
            img_x = img[:, ::-1, :]
            matimg = img_x.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))
            pass
        elif self.combox.currentText() == '原点对称':
            img = cv2.imread(self.imagepath[0])
            img_x = img[::-1, ::-1, :]
            matimg = img_x.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))
            pass
        elif self.combox.currentText() == '图片取1/4':
            #self.lab.setFixedSize(400, 400)
            img = cv2.imread(self.imagepath[0])
            img_x = img[::2, ::2, :]
            matimg = img_x.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(bgrimg.width(), bgrimg.height()))
            #self.lab.setFixedSize(200,200)
            pass
        elif self.combox.currentText() == '截取':
            img = cv2.imread(self.imagepath[0])
            face = np.ones((101, 101, 3))
            face = img[220:400, 250:350]
            img_x = face
            matimg = img_x.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))
            pass

    def imageshow(self):
        img = cv2.imread(self.imagepath[0])
        matimg = img.astype(np.uint8)  # bgr
        rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
        bgrimg = rgbimg.rgbSwapped()
        self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginWin()
    win.show()

