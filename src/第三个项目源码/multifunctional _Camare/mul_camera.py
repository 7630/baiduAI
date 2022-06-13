#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 14:37
# @Author  : 廖荣森
# @File    : mul_camera.py
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
from aip import AipBodyAnalysis

class CameraVideo(QWidget):
    def __init__(self):
        super(CameraVideo, self).__init__()
        self.resize(800, 800)
        self.setWindowTitle("多功能相机")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/6.jpg").scaled(self.width(), self.height())))
        # palette = palette.scaled(Cam.width(), Cam.height())
        self.setPalette(palette)
        #定义一些全局变量
        self.facenum = 1
        self.timer_camera = QTimer()
        self.videocap = []
        self.cap = []
        self.out = []
        self.img = ""
        self.imagepath=[]
        self.flag = False
        self.videoFlag = 0
        #定义标签和按钮
        self.lab = QLabel(self)
        self.lab.setText("  ")



        self.lab1 = QLabel(self)
        self.lab1.setText(" ")
        img_path = './icon/12.jpg'  # 图片路径
        self.lab1.setStyleSheet("QLabel{\n"
                                    "border-image:url(\"%s\");\n"
                                    "}" % img_path)
        self.lab1.setFixedSize(150, 150)
        #调用级联分类器，相机中暂无使用，打开后可以框出人脸
        self.faceCascade = cv2.CascadeClassifier('./facexml/haarcascade_frontalface_alt.xml')


        # self.lab2 = QLabel(self)
        # img_path = './icon/6.jpg'  # 图片路径
        # self.lab2.setStyleSheet("QLabel{\n"
        #                         "border-image:url(\"%s\");\n"
        #
        #                         "}" % img_path)
        # self.lab2.move(0, 0)
        # self.lab2.resize(800, 800)

        self.btn_open = QPushButton(self)
        self.btn_open.setToolTip("打开相机")
        self.btn_open.setMaximumSize(60, 60)
        self.btn_open.setMinimumSize(60, 60)
        img_path = './icon/dakaixiangji.png'  # 图片路径
        self.btn_open.setStyleSheet("QPushButton{\n"
                                    "border-image:url(\"%s\");\n"
                                    "}" % img_path)
        self.btn_open.setFixedSize(70, 60)

        self.btn1 = QPushButton(self)
        self.btn1.setToolTip("打开相册")
        self.btn1.setMaximumSize(50, 50)
        self.btn1.setMinimumSize(50, 50)
        img_path = './icon/dakaixiangce.png'  # 图片路径
        self.btn1.setStyleSheet("QPushButton{\n"
                                "border-image:url(\"%s\");\n"
                                "}" % img_path)
        self.btn1.setFixedSize(70, 60)
        #self.lab1.setToolTip('打开相册')

        self.btn_capture = QPushButton(self)
        self.btn_capture.setToolTip("拍照")
        self.btn_capture.setMaximumSize(50, 50)
        self.btn_capture.setMinimumSize(50, 50)
        img_path = './icon/paizhao.png'  # 图片路径
        self.btn_capture.setStyleSheet("QPushButton{\n"
                                       "border-image:url(\"%s\");\n"
                                       "}" % img_path)
        self.btn_capture.setFixedSize(70, 60)

        self.btn_recorder = QPushButton(self)
        self.btn_recorder.setToolTip("录像")
        self.btn_recorder.setMaximumSize(50, 50)
        self.btn_recorder.setMinimumSize(50, 50)
        img_path = './icon/luxiang.png'  # 图片路径
        self.btn_recorder.setStyleSheet("QPushButton{\n"
                                        "border-image:url(\"%s\");\n"
                                        "}" % img_path)
        self.btn_recorder.setFixedSize(70, 60)

        self.btn_close = QPushButton(self)
        self.btn_close.setToolTip("关闭")
        self.btn_close.setMaximumSize(50, 50)
        self.btn_close.setMinimumSize(50, 50)
        img_path = './icon/guanbi.png'  # 图片路径
        self.btn_close.setStyleSheet("QPushButton{\n"
                                     "border-image:url(\"%s\");\n"
                                     "}" % img_path)
        self.btn_close.setFixedSize(70, 60)

        self.btn_food = QPushButton(self)
        self.btn_food.setToolTip("菜品识别")
        self.btn_food.setMaximumSize(50, 50)
        self.btn_food.setMinimumSize(50, 50)
        img_path = './icon/caipingshibie.png'  # 图片路径
        self.btn_food.setStyleSheet("QPushButton{\n"
                                    "border-image:url(\"%s\");\n"
                                    "}" % img_path)
        self.btn_food.setFixedSize(70, 60)

        self.btn_anime = QPushButton(self)
        self.btn_anime.setToolTip("人像动漫化")
        self.btn_anime.setMaximumSize(50, 50)
        self.btn_anime.setMinimumSize(50, 50)
        img_path = './icon/renwudongmanhua.png'  # 图片路径
        self.btn_anime.setStyleSheet("QPushButton{\n"
                                     "border-image:url(\"%s\");\n"
                                     "}" % img_path)
        self.btn_anime.setFixedSize(70, 60)

        self.btn_animal = QPushButton(self)
        self.btn_animal.setToolTip("动物识别")
        self.btn_animal.setMaximumSize(50, 50)
        self.btn_animal.setMinimumSize(50, 50)
        img_path = './icon/dongwushibie.png'  # 图片路径
        self.btn_animal.setStyleSheet("QPushButton{\n"
                                      "border-image:url(\"%s\");\n"
                                      "}" % img_path)
        self.btn_animal.setFixedSize(70, 60)

        self.btn_style = QPushButton(self)
        self.btn_style.setToolTip("图像风格转换")
        self.btn_style.setMaximumSize(50, 50)
        self.btn_style.setMinimumSize(50, 50)
        img_path = './icon/tuxiangfengge.png'  # 图片路径
        self.btn_style.setStyleSheet("QPushButton{\n"
                                     "border-image:url(\"%s\");\n"
                                     "}" % img_path)
        self.btn_style.setFixedSize(70, 60)

        self.combox = QComboBox(self)
        self.combox.addItems(['cartoon','pencil','color_pencil','warm','wave','lavender','mononoke','scream','gothic'])
        self.combox.setFixedSize(100,40)

        #设计布局，放button
        vlayout = QVBoxLayout(self)
        vlayout.addWidget(self.lab)

        hlayout = QHBoxLayout(self)
        vlayout.addLayout(hlayout)
        vlayout1 = QVBoxLayout(self)
        hlayout.addLayout(vlayout1)

        hlayout1 =QHBoxLayout(self)
        vlayout1.addLayout(hlayout1)
        hlayout2 = QHBoxLayout(self)
        vlayout1.addLayout(hlayout2)
        hlayout1.addWidget(self.btn_open)
        hlayout1.addWidget(self.btn1)
        hlayout1.addWidget(self.btn_capture)
        hlayout1.addWidget(self.btn_recorder)
        hlayout1.addWidget(self.btn_close)
        hlayout.addWidget(self.lab1)
        hlayout2.addWidget(self.btn_food)
        hlayout2.addWidget(self.btn_anime)
#        hlayout2.addWidget(self.btn_sky)
        hlayout2.addWidget(self.btn_animal)
        hlayout2.addWidget(self.btn_style)
        hlayout2.addWidget(self.combox)

        #所有的槽函数
        self.btn_open.clicked.connect(self.open_slot)
        self.btn1.clicked.connect(self.OpenFile)                    #打开相册的槽函数
        self.btn_capture.clicked.connect(self.capture_slot)
        self.btn_close.clicked.connect(self.close_slot)
        self.btn_food.clicked.connect(self.Dishes_identify)
        self.btn_animal.clicked.connect(self.animal_identify)
        self.btn_anime.clicked.connect(self.Anime)
        self.btn_style.clicked.connect(self.style_trans)
        self.btn_recorder.clicked.connect(self.recortVideo)

    #打开相机  以定时器的方法
    def open_slot(self):
        print("open_slot")
        self.cap = cv2.VideoCapture(0)
        self.timer_camera.start(10)
        self.timer_camera.timeout.connect(self.readFrame)
    def readFrame(self):
        if(self.cap.isOpened()):
            self.flag =True
            ret,self.img = self.cap.read()
            self.img = cv2.flip(self.img, 1)
            if ret:
                grap = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                # faces = self.faceCascade.detectMultiScale(self.img)
                # for (x, y, w, h) in faces:
                #     cv2.rectangle(grap, (x, y), (x + w, y + h), (0, 255, 0))
                    # self.fact_path = "./faceimg/face{}.jpg".format(self.num)
                    # cv2.imwrite(self.fact_path, grap[y:y + h, x:x + w])
                height,width,channel = grap.shape
                bytessize = channel*width
                image = QImage(grap.data,width,height,bytessize,
                              QImage.Format_RGB888).scaled(self.lab.width(),self.lab.height())
                self.lab.setPixmap(QPixmap.fromImage(image))
            else:
                self.cap.release()
                self.timer_camera.stop()
        pass
    #打开本地相册
    def OpenFile(self):
        if(self.flag):
            self.cap.release()
        self.imagepath = QFileDialog.getOpenFileName(None, "选择图片", "./CameraPhoto", "All File(*);;")
        if self.imagepath[0]:
            img = cv2.imread(self.imagepath[0])
            matimg = img.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))
            self.flag = False
        else:
            QMessageBox.warning(self,"警告","没有导入照片")
        pass
    #关闭相机
    def close_slot(self):
        print("close_slot")
        if self.cap != []:
            self.cap.release()
            self.timer_camera.stop()
            pass
        else:
            print("error")
        pass
    #拍照
    def capture_slot(self):
        print("capture_slot")
        # if self.cap!=[]:
        self.cap = cv2.VideoCapture(0)
        self.OK, self.img = self.cap.read()
        img = cv2.flip(self.img, 1)
        localDataTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
        # print(localDataTime)  以本地时间作为存储名字
        cv2.imwrite("./CameraPhoto/" + str(localDataTime) + ".jpg", img)
        matimg = img.astype(np.uint8)  # bgr
        rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
        bgrimg = rgbimg.rgbSwapped()
        self.lab1.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab1.width(), self.lab1.height()))
        # else:
        #     QMessageBox.warning(self, "警告", "相机还未打开")
    #token令牌
    def get_access_token(self,client_id, client_secret):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            client_id, client_secret)
        response = requests.get(host)
        if response:
           # print(response.json())
            return response.json()['access_token']
        pass
   #菜品识别
    def Dishes_identify(self):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/dish"
        if (self.cap or self.imagepath):
            if self.cap.isOpened():
                img = cv2.imwrite("./CameraPhoto/dish.jpg", self.img)
                f = open('./CameraPhoto/dish.jpg', 'rb')
                self.cap.release()
            elif self.imagepath:
                f = open(self.imagepath[0], 'rb')
            img = base64.b64encode(f.read())
            params = {"image": img, "top_num": 5}
            # 令牌
            access_token = self.get_access_token(client_id="fldXYAM1tIDBItLLYBmpGAre",
                                                 client_secret="T6d3x1XcvtSWMQ3RGVr82sNZ5oTGYCju")
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)
            if response:
                # print(response.json()['result'][0]['name'])
                QMessageBox.information(self, '菜品', response.json()['result'][0]['name'])
        else:
            QMessageBox.warning(self, "警告", "请打开相机或者导入照片")

    #动物识别
    def animal_identify(self):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
        if (self.cap or self.imagepath):
            if self.cap.isOpened():
                img = cv2.imwrite("./CameraPhoto/animal.jpg", self.img)
                f = open('./CameraPhoto/animal.jpg', 'rb')
                self.cap.release()
            elif self.imagepath:
                f = open(self.imagepath[0], 'rb')
            img = base64.b64encode(f.read())
            params = {"image": img, "top_num": 5}
            # 令牌
            access_token = self.get_access_token(client_id="fldXYAM1tIDBItLLYBmpGAre",
                                                 client_secret="T6d3x1XcvtSWMQ3RGVr82sNZ5oTGYCju")
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)
            if response:
                # print(response.json()['result'][0]['name'])
                QMessageBox.information(self, '动物', response.json()['result'][0]['name'])
        else:
            QMessageBox.warning(self, "警告", "请打开相机或者导入照片")
    #人像动漫化
    def Anime(self):
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
        if (self.cap or self.imagepath):
            if self.cap:
                img = cv2.imwrite("./CameraPhoto/anime.jpg", self.img)
                f = open('./CameraPhoto/anime.jpg', 'rb')
                self.cap.release()
            elif self.imagepath:
                f = open(self.imagepath[0], 'rb')
            img = base64.b64encode(f.read())
            params = {"image": img, "top_num": 5}
            access_token = self.get_access_token(client_id="CA3svz4VbftzGxIIMt455OdA",
                                                 client_secret="fegj6ZMN9XAOz7EHOH94pdAbXF6Z7mm0")
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)
            localDataTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
            animePath = "./CameraPhoto/" + str(localDataTime) + ".jpg"
            f = open(animePath, "wb")
            f.write(base64.b64decode(response.json()['image']))
            img = cv2.imread(animePath)
            matimg = img.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab1.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab1.width(), self.lab1.height()))
        else:
            QMessageBox.warning(self, "警告", "请打开相机或者导入照片")
    #图像风格
    def style_trans(self):
        request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/style_trans"
        if (self.cap or self.imagepath):
            if self.cap:
                img = cv2.imwrite("./CameraPhoto/style.jpg", self.img)
                f = open('./CameraPhoto/style.jpg', 'rb')
                self.cap.release()
            elif self.imagepath:
                f = open(self.imagepath[0], 'rb')
            img = base64.b64encode(f.read())
            params = {"image": img, "option": "{}".format(self.combox.currentText())}
            access_token = self.get_access_token(client_id="CA3svz4VbftzGxIIMt455OdA",
                                                 client_secret="fegj6ZMN9XAOz7EHOH94pdAbXF6Z7mm0")
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)
            localDataTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
            animePath = "./CameraPhoto/" + str(localDataTime) + ".jpg"
            # if response:
            #     print(response.json())
            f = open(animePath, "wb")
            f.write(base64.b64decode(response.json()['image']))
            img = cv2.imread(animePath)
            matimg = img.astype(np.uint8)  # bgr
            rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
            bgrimg = rgbimg.rgbSwapped()
            self.lab1.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab1.width(), self.lab1.height()))
        else:
            QMessageBox.warning(self, "警告", "请打开相机或者导入照片")
        #录像
    def recortVideo(self):
        self.videoFlag+=1
        if self.videoFlag%2==1:
            self.cap = cv2.VideoCapture(0)
            fourCC = cv2.VideoWriter_fourcc(*'MJPG')
            localDataTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
            self.out = cv2.VideoWriter("./CameraPhoto/video/" + str(localDataTime) + ".avi", fourCC, 5, (640, 480))
           # self.out = cv2.VideoWriter("./video/jack.avi", fourCC, 5, (640, 480))
            while (self.cap.isOpened()):
                ret, frame = self.cap.read()
                frame = cv2.flip(frame, 1)
                self.out.write(frame)
                matimg = frame.astype(np.uint8)  # bgr
                rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
                bgrimg = rgbimg.rgbSwapped()
                self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))
               # cv2.imshow("jack", frame)
                code = cv2.waitKey(100)
                if code == 27:
                    break
                else:
                    continue
            self.cap.release()
            self.out.release()
        else:
            self.videoFlag = True
            self.cap.release()
            self.out.release()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Cam = CameraVideo()

    Cam.show()
    sys.exit(app.exec_())