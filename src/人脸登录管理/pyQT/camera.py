#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 15:04
# @Author  : 廖荣森
# @File    : camera.py

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

from  loginWindet import *

class Video(QWidget):
    def __init__(self):
        super(Video,self).__init__()

        self.num = 1
        self.cap = []
        self.img = []
        self.OK = False
        self.timer_camera = QTimer()
        self.videocap=[]
        self.fact_path = ""
        self.faceCascade = cv2.CascadeClassifier(r'D:\Users\12466\PycharmProjects\pythonProject\pyQT\facexml\haarcascade_frontalface_alt.xml')

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
        vlayout.addWidget(self.btn_close)

        vlayout.addWidget(self.lab1)
        hlayout.addLayout(vlayout)

        self.btn_open.clicked.connect(self.open_slot)
        self.btn_capture.clicked.connect(self.capture_slot)
        self.btn_recorder.clicked.connect(self.recorder_slot)
        self.btn_close.clicked.connect(self.close_slot)
        self.btn_cai.clicked.connect(self.collect)
        self.btn_train.clicked.connect(self.train_slot)
        self.btn_log.clicked.connect(self.log_slot)
    pass

    def open_slot(self):
        print("open_slot")
        self.cap = cv2.VideoCapture(0)
        self.timer_camera.start(10)
        self.timer_camera.timeout.connect(self.readFrame)
        # self.faceCascade = cv2.CascadeClassifier(r'D:\Users\12466\PycharmProjects\pythonProject\pyQT\facexml\haarcascade_frontalface_alt.xml')
        # self.OK =True
        # while self.OK:
        #     self.OK, img = self.cap.read()  # mat  imread
        #     img = cv2.flip(img, 1)
        #     grap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     # ret,binary = cv2.threshold(grap,0,255,cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
        #     # 图像检测
        #     faces = self.faceCascade.detectMultiScale(grap)
        #     #print(img)
        #     for (x, y, w, h) in faces:
        #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0))  # BGR
        #     matimg = img.astype(np.uint8)  # bgr
        #     rgbimg = QImage(matimg.data, matimg.shape[1], matimg.shape[0], matimg.shape[1] * 3, QImage.Format_RGB888)
        #     bgrimg = rgbimg.rgbSwapped()
        #     # self.lab.setStyleSheet("border-image: url("+self.imagepath[0]+")")
        #     self.lab.setPixmap(QPixmap.fromImage(bgrimg).scaled(bgrimg.width(), bgrimg.height()))
        #    # cv2.imshow("face", img)
        #     key = cv2.waitKey(1)
        #     if key == 27:
        #         self.OK = False
        #         break
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
        #print("1111111111")
        if(self.cap.isOpened()):
            ret,self.img = self.cap.read()
            #print("img",self.img)
           # print(ret)
            if ret:
                grap = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                height,width,channel = grap.shape
                bytessize = channel*width
                image = QImage(grap.data,width,height,bytessize,
                              QImage.Format_RGB888).scaled(self.lab.width(),self.lab.height())
                self.lab.setPixmap(QPixmap.fromImage(image))
                # self.fact_path = "./faceimg/face{}.jpg".format(self.num)
                # cv2.imwrite(self.fact_path,self.img)
                # self.num +=1
            else:
                self.cap.release()
                self.timer_camera.stop()
            # if self.num>=100:
            #     self.num = 1
            #     self.cap.release()
            #     self.timer_camera.stop()
            #     print("结束采集")
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
            # print("img",self.img)
            # print(ret)
            if ret:
                grap = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                # faces = self.faceCascade.detectMultiScale(self.img,1.1,cv2.CASCADE_SCALE_IMAGE,(200,200),(300,300))
                faces = self.faceCascade.detectMultiScale(self.img)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myVideo = Video()
    LoginWin = LoginWin()
    myVideo.show()
    sys.exit(app.exec_())