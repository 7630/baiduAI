#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 14:33
# @Author  : 廖荣森
# @File    : facewin.py
import cv2
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage, QMovie, QPixmap
import numpy as np


class facewin(QWidget):
    my_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.PlayUiInit()

    def PlayUiInit(self):
        self.setWindowTitle("播放模块")
        self.setFixedSize(600, 600)
        self.btn = QPushButton(self)
        self.btn.setText("打开")
        self.btn.move(500, 400)
        self.lab = QLabel(self)
        self.lab.resize(500, 600)
        self.btn.clicked.connect(self.play)

    def play(self):
        cap = cv2.VideoCapture(0)
        # 调用级联器识别图像
        faceCascade = cv2.CascadeClassifier(r'D:\Users\12466\PycharmProjects\pythonProject\pyQT\facexml\haarcascade_frontalface_alt.xml')
        OK = True
        while OK:
            OK, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0))
            matimg = img.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            # self.lab.setStyleSheet("border-image: url("+self.imagepath[0]+")")
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(bgrimg.width(), bgrimg.height()))
            key = cv2.waitKey(1)
            if key == 27:
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    facewin = facewin()
    facewin.show()
    sys.exit(app.exec_())
