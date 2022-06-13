#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 17:19
# @Author  : 廖荣森
# @File    : faceAIlogin.py

#绘制 相机界面 显示区域 label 按钮 打开 关闭 拍照

#把OpenCV 获取的mat格式的 图片 放到label进行显示
#from PyQt5 import  QtWidgets

#人脸登录
#1、操作摄像头 2、注册（人脸照片采集拍照叉多张不同角度的照片）3、保存标注 训练 模型文件
#训练 train 样本数据（训练集 ，测试集） train

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
from  loginWindet import *

class Video(QWidget):
    def __init__(self):
        super(Video,self).__init__()
        self.flag = 0
        self.num = 1
        self.cap = []
        self.img = []
        self.OK = False
        self.timer_camera = QTimer()
        self.videocap=[]
        self.fact_path = ""
        self.faceCascade = cv2.CascadeClassifier(r'D:\Users\12466\PycharmProjects\pythonProject\multifunctional _Camare\facexml\haarcascade_frontalface_alt.xml')

        self.resize(800,800)
        self.setWindowTitle("相机")

        self.lab = QLabel(self)
        self.lab.setText("打开摄像头")
        self.lab1 = QLabel(self)
        self.lab1.setText("拍照")
        self.lab1.setFixedSize(150,150)

        self.btn_open = QPushButton(self)
        self.btn_open.setText("打开")
        self.btn_open.setFixedSize(150,50)
        self.btn_close = QPushButton(self)
        self.btn_close.setText("关闭")
        self.btn_close.setFixedSize(150,50)
        self.btn_capture = QPushButton(self)
        self.btn_capture.setText("拍照")
        self.btn_capture.setFixedSize(150,50)
        self.btn_recorder = QPushButton(self)
        self.btn_recorder.setText("录像")
        self.btn_recorder.setFixedSize(150,50)
        self.btn_cai = QPushButton(self)
        self.btn_cai.setText("采集")
        self.btn_cai.setFixedSize(150, 50)

        self.btn_train = QPushButton(self)
        self.btn_train.setText("训练")
        self.btn_train.setFixedSize(150, 50)

        self.btn_cofig = QPushButton(self)
        self.btn_cofig.setText("人脸检测")
        self.btn_cofig.setFixedSize(150, 50)

        self.btn_log = QPushButton(self)
        self.btn_log.setText("登录")
        self.btn_log.setFixedSize(150, 50)

        hlayout = QHBoxLayout(self)
        hlayout.addWidget(self.lab)

        vlayout = QVBoxLayout(self)

        vlayout.addWidget(self.btn_open)
        vlayout.addWidget(self.btn_capture)
        vlayout.addWidget(self.btn_recorder)
        vlayout.addWidget(self.btn_cai)
        vlayout.addWidget(self.btn_train)
        vlayout.addWidget(self.btn_log)
        vlayout.addWidget(self.btn_cofig)
        vlayout.addWidget(self.btn_close)

        vlayout.addWidget(self.lab1)
        hlayout.addLayout(vlayout)

        self.btn_open.clicked.connect(self.open_slot)
        self.btn_capture.clicked.connect(self.capture_slot)
        self.btn_recorder.clicked.connect(self.recorder_slot)
        self.btn_close.clicked.connect(self.close_slot)
        self.btn_cai.clicked.connect(self.collect)
        self.btn_train.clicked.connect(self.train_slot)
        self.btn_cofig.clicked.connect(self.cofig_slot)
        self.btn_log.clicked.connect(self.log_slot)
    pass

    def open_slot(self):
        print("open_slot")
        self.cap = cv2.VideoCapture(0)
        self.timer_camera.start(10)
        self.timer_camera.timeout.connect(self.readFrame)

    def capture_slot(self):
        print("capture_slot")
        self.cap = cv2.VideoCapture(0)
        self.OK, self.img = self.cap.read()
        img = cv2.flip(self.img, 1)
        datatime = time.time()
        cv2.imwrite("./" + str(datatime) + ".jpg", img)
        matimg = img.astype(np.uint8)  # bgr
        rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
        bgrimg = rgbimg.rgbSwapped()
        self.lab1.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab1.width(), self.lab1.height()))
    def close_slot(self):
        print("close_slot")
        if self.cap !=[]:
            self.cap.release()
            self.timer_camera.stop()
            pass
        else:
            print("error")
        pass
    def readFrame(self):
        if(self.cap.isOpened()):
            ret,self.img = self.cap.read()
            if ret:
                grap = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                faces = self.faceCascade.detectMultiScale(self.img)
                for (x, y, w, h) in faces:
                    cv2.rectangle(grap, (x, y), (x + w, y + h), (0, 255, 0))
                    self.fact_path = "./faceimg/face{}.jpg".format(self.num)
                    cv2.imwrite(self.fact_path, grap[y:y + h, x:x + w])
                height,width,channel = grap.shape
                bytessize = channel*width
                image = QImage(grap.data,width,height,bytessize,
                              QImage.Format_RGB888).scaled(self.lab.width(),self.lab.height())
                self.lab.setPixmap(QPixmap.fromImage(image))
            else:
                self.cap.release()
                self.timer_camera.stop()
        pass
    def recorder_slot(self):
        print("recorder_slot")
        if self.num == 1:
            print("luzhi")
            self.videocap = cv2.VideoWriter(r'D:\Users\12466\PycharmProjects\pythonProject\pyQT' + str(time.time()) + '.mp4',
                                    cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 30, (640, 480))
            self.num +=1
        elif self.num%2 == 0:
            self.videocap.release()
            time.sleep(1)
    #采集人脸
    def collect(self):
        print("collect")
        self.cap = cv2.VideoCapture(0)
        self.timer_camera.start(10)
        self.timer_camera.timeout.connect(self.collectFrame)
    def collectFrame(self):
        if (self.cap.isOpened()):
            ret, self.img = self.cap.read()
            if ret:
                grap = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                # faces = self.faceCascade.detectMultiScale(self.img,1.1,cv2.CASCADE_SCALE_IMAGE,(200,200),(300,300))
                faces = self.faceCascade.detectMultiScale(self.img)
                #画框
                for (x,y,w,h) in faces:
                    cv2.rectangle(grap,(x,y),(x+w,y+h),(0,255,0))
                    self.fact_path = "./faceimg/face{}.jpg".format(self.num)
                    cv2.imwrite(self.fact_path, grap[y:y+h,x:x+w])
                    self.num += 1

                height, width, channel = grap.shape
                bytessize = channel * width
                image = QImage(grap.data, width, height, bytessize,
                               QImage.Format_RGB888).scaled(self.lab.width(), self.lab.height())
                self.lab.setPixmap(QPixmap.fromImage(image))
            else:
                self.cap.release()
                self.timer_camera.stop()
            if self.num >= 100:
                self.num = 1
                self.cap.release()
                self.timer_camera.stop()
                print("结束采集")
        pass
    #人脸训练
    def train_slot(self):
        #训练集
        face_list = []
        ids = []
        face_path = "./faceimg/"
        img_list = os.listdir(face_path) #100图片数据
        #创建 脸部识别器
        facerecognizer = cv2.face.LBPHFaceRecognizer_create()
        for i in img_list:
            print(i)
            img = cv2.imread(face_path+i)
            #灰度处理，降低图片维度
            img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            face_list.append(img_gray)

            ids.append(0)
            pass
        #模型训练
        facerecognizer.train(face_list,np.array(ids))

        facerecognizer.write("./face.yml")
        print("模型训练完成")
    #人脸登录
    def log_slot(self):
        print("登录")
        count = 0
        facerecognizer = cv2.face.LBPHFaceRecognizer_create()
        facerecognizer.read("./face.yml")

        self.cap = cv2.VideoCapture(0)
        self.OK = True
        while self.OK:
            ret , img = self.cap.read()  # mat  imread
            if ret:
                grap = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                faces = self.faceCascade.detectMultiScale(grap)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))  # BGR

                    #模型预测
                    userid, confidence =facerecognizer.predict(grap[y:y+h,x:x+w])
                    print(userid,confidence)
                    if confidence < 50:
                        count+=1
                matimg = img.astype(np.uint8)  # bgr
                rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3,
                                QImage.Format_RGB888)
                bgrimg = rgbimg.rgbSwapped()
                self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(self.lab.width(), self.lab.height()))
                #cv2.imshow("face",img)
            else:
                break
            key = cv2.waitKey(10)
            if count > 10:
                print("登录成功")
                self.OK = False
                self.cap.release()
                count = 0
                #LoginWin = LoginWin()
                LoginWin.show()
                self.close()
            if key == 27:
                self.OK = False
                break

    def get_access_token(self,client_id, client_secret):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
            client_id, client_secret)
        response = requests.get(host)
        if response:
           # print(response.json())
            return response.json()['access_token']
        pass

    def cofig_slot(self):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
        img1 = cv2.imwrite("./1.jpg", self.img)
        f1 = open('./1.jpg', 'rb')
        img1 = base64.b64encode(f1.read())
        f2 = open('./myself.jpg', 'rb')
        img2 = base64.b64encode(f2.read())
        params = json.dumps([
            {
                "image": str(img1,'utf-8'),
                "image_type": "BASE64",
                "face_type": "LIVE",
                "quality_control": "LOW",
            },
            {
                "image": str(img2,'utf-8'),
                "image_type": "BASE64",
                "face_type": "LIVE",
                "quality_control": "LOW",
            }
        ])
        params = eval(params)
        access_token = self.get_access_token(client_id= "6m45tPZplBxAuPjbPGOeqyxP", client_secret="6SkTelgcOKBK6UTgh3cOQUwwhvVWnvBQ")
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, json=params, headers=headers)
        #print(response.json())
        if response.json()['result']['score'] > 90:
            # print(response.json())
            print("通过仔细的识别和判断，确认过{}%的眼神，你是对的人".format(response.json()['result']['score']))
            self.cap.release()
            LoginWin.show()
            self.close()
            #self.flag = 1
        else:
            print("我不认识你，所以你肯定是傻逼，匹配度{}%".format(response.json()['result']['score']))
           # self.flag = 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myVideo = Video()
    LoginWin = LoginWin()
    myVideo.show()
    sys.exit(app.exec_())