#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 9:10
# @Author  : 廖荣森
# @File    : register.py
#from mul_camera import *
#from denglu import *
import winMa
import sys
import  cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage, QMovie, QPixmap
import numpy as np
from PyQt5.QtCore import *
import  time
import os
from  PyQt5.QtGui import  *
from PyQt5.QtWidgets import QApplication
import json
import requests
import base64

class VideoRegister(QWidget):
    def __init__(self):
        super(VideoRegister, self).__init__()
        self.facenum=1
        self.timer_camera = QTimer()
        self.videocap = []
        self.cap = []
        self.img = []
        self.flag = False
        self.OK = False
        self.face_list = []
        self.face_path = []
        self.resize(800, 800)
        self.setWindowTitle("人脸注册")
        self.faceCascade = cv2.CascadeClassifier('./facexml/haarcascade_frontalface_alt.xml')

        self.lab = QLabel(self)
        self.lab.setText("  ")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/13.jpg").scaled(self.width(), self.height())))
        # palette = palette.scaled(Cam.width(), Cam.height())
        self.setPalette(palette)


        self.btn_open = QPushButton(self)
        self.btn_open.setToolTip("打开")
        self.btn_open.setMaximumSize(65, 65)
        self.btn_open.setMinimumSize(65, 65)
        img_path = 'icon/dakai.png'  # 图片路径
        self.btn_open.setStyleSheet("QPushButton{\n"
                                    "border-image:url(\"%s\");\n"
                                    "}" % img_path)
        self.btn_open.setFixedSize(80, 50)

        self.btn_capture = QPushButton(self)
        self.btn_capture.setToolTip("人脸注册")
        self.btn_capture.setMaximumSize(30, 30)
        self.btn_capture.setMinimumSize(30, 30)
        img_path = 'icon/renlianzhuce.png'  # 图片路径
        self.btn_capture.setStyleSheet("QPushButton{\n"
                                       "border-image:url(\"%s\");\n"
                                       "}" % img_path)
        self.btn_capture.setFixedSize(80, 50)


        self.btn_cofig = QPushButton(self)
        self.btn_cofig.setToolTip("人脸登录")
        self.btn_cofig.setMaximumSize(30, 30)
        self.btn_cofig.setMinimumSize(30, 30)
        img_path = 'icon/renliandenglu.png'  # 图片路径
        self.btn_cofig.setStyleSheet("QPushButton{\n"
                                     "border-image:url(\"%s\");\n"
                                     "}" % img_path)
        # self.btn_cofig.setText("人脸登录")
        self.btn_cofig.setFixedSize(80, 50)

        self.btn_close = QPushButton(self)
        self.btn_close.setToolTip("关闭")
        self.btn_close.setMaximumSize(30, 30)
        self.btn_close.setMinimumSize(30, 30)
        img_path = 'icon/guanbi.png'  # 图片路径
        self.btn_close.setStyleSheet("QPushButton{\n"
                                     "border-image:url(\"%s\");\n"
                                     "}" % img_path)
        # self.btn_close.setText("关闭")
        self.btn_close.setFixedSize(80, 50)

        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.lab)

        hlayout = QHBoxLayout(self)
        vlayout.addLayout(hlayout)
        hlayout.addWidget(self.btn_open)
        hlayout.addWidget(self.btn_capture)
        hlayout.addWidget(self.btn_cofig)   #人脸登录
        hlayout.addWidget(self.btn_close)
        self.btn_open.clicked.connect(self.open_slot)
        self.btn_capture.clicked.connect(self.capture_slot) #注册的槽函数
        self.btn_cofig.clicked.connect(self.cofig_slot)     #人脸登录
        self.btn_close.clicked.connect(self.close_slot)
    def open_slot(self):
        print("open_slot")
        self.cap = cv2.VideoCapture(0)
        self.timer_camera.start(10)
        self.timer_camera.timeout.connect(self.readFrame)

    def readFrame(self):
        if (self.cap.isOpened()):
            ret, self.img = self.cap.read()
            self.img = cv2.flip(self.img, 1)
            if ret:
                grap = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                faces = self.faceCascade.detectMultiScale(self.img)
                for (x, y, w, h) in faces:
                    cv2.rectangle(grap, (x, y), (x + w, y + h), (0, 255, 0))
                    # self.fact_path = "./faceimg/face{}.jpg".format(self.num)
                    # cv2.imwrite(self.fact_path, grap[y:y + h, x:x + w])
                height, width, channel = grap.shape
                bytessize = channel * width
                image = QImage(grap.data, width, height, bytessize,
                                   QImage.Format_RGB888).scaled(self.lab.width(), self.lab.height())
                self.lab.setPixmap(QPixmap.fromImage(image))
            else:
                self.cap.release()
                self.timer_camera.stop()
        pass

    def capture_slot(self):
        if self.cap != []:
            print("capture_slot")
            self.cap = cv2.VideoCapture(0)
            self.OK, self.img = self.cap.read()
            img = cv2.flip(self.img, 1)
            print(img)
            # datatime = time.time()

            self.face_path = "./image/face{}.jpg".format(self.facenum)
            self.facenum += 1
            cv2.imwrite(self.face_path, img)
        else:
            QMessageBox.warning(self, "警告", "相机还未打开")
        #print(self.facenum)
        #print(self.face_path)
        #cv2.imwrite("./image" + str(datatime) + ".jpg", img)
        #matimg = img.astype(np.uint8)  # bgr
        #rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
        #bgrimg = rgbimg.rgbSwapped()
        # self.lab1.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab1.width(), self.lab1.height()))
    def get_access_token(self,client_id, client_secret):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            client_id, client_secret)
        response = requests.get(host)
        if response:
           # print(response.json())
            return response.json()['access_token']
        pass

    def cofig_slot(self):
        if self.cap != []:
            request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
            # img1 = cv2.imwrite("./1.jpg", self.img)
            cv2.imwrite("./1.jpg", self.img)
            f1 = open('./1.jpg', 'rb')
            img1 = base64.b64encode(f1.read())
            face_list = []
            ids = []
            # f2 = open('image/myself.jpg', 'rb')
            face_path = "./image/"
            img_list = os.listdir(face_path)
            for i in img_list:
                f2 = open(face_path + i, 'rb')
                img2 = base64.b64encode(f2.read())
                params = json.dumps([
                    {
                        "image": str(img1, 'utf-8'),
                        "image_type": "BASE64",
                        "face_type": "LIVE",
                        "quality_control": "LOW",
                    },
                    {
                        "image": str(img2, 'utf-8'),
                        "image_type": "BASE64",
                        "face_type": "LIVE",
                        "quality_control": "LOW",
                    }
                ])
                params = eval(params)
                access_token = self.get_access_token(client_id="6m45tPZplBxAuPjbPGOeqyxP",
                                                     client_secret="6SkTelgcOKBK6UTgh3cOQUwwhvVWnvBQ")
                request_url = request_url + "?access_token=" + access_token
                headers = {'content-type': 'application/json'}
                response = requests.post(request_url, json=params, headers=headers)
                # print(response.json())
                if response.json()['result']:
                    if response.json()['result']['score'] > 90:
                        # print(response.json())
                        # print("通过仔细的识别和判断，确认过{}%的眼神，你是对的人".format(response.json()['result']['score']))
                        self.flag = True
                        break
                    # self.cap.release()
                    # self.close()
                # else:
                #     print("我不认识你，所以你肯定是傻逼，匹配度{}%".format(response.json()['result']['score']))
            print(self.flag)
            if self.flag:
                print("通过仔细的识别和判断，确认过{}%的眼神，你是对的人".format(response.json()['result']['score']))
                self.close()
                winMa.cam.show()
                self.cap.release()

            else:
                print("目前匹配度{}%，难以识别是否为管理员，是否注册".format(response.json()['result']['score']))
        else:
            QMessageBox.warning(self,"警告","相机还未打开")


    def close_slot(self):
        print("close_slot")
        if self.cap != []:
            self.cap.release()
            self.timer_camera.stop()
            winMa.login.show()
            self.close()
            pass
        else:
            self.close()
            winMa.login.show()
            print("error")
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myVideo = VideoRegister()

    # registerWin = CameraVideo()
    # login = LoginWin()
    myVideo.show()
    sys.exit(app.exec_())