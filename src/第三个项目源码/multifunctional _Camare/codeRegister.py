#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 11:05
# @Author  : wx
# @File    : zhuce.py
#from denglu import *
from  winMa import *
import winMa
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.RegisterUiInit()
        self.file_path = './registerInformation/users.txt'
        self.users = []


    def RegisterUiInit(self):
        self.setWindowTitle("账号注册")
        self.setFixedSize(800,800)

        self.lab = QLabel(self)
        self.lab.setText("")

        self.lab.move(0, 0)
        self.lab.resize(800, 800)
        #self.lab.setStyleSheet('1.jpg')

        self.lab1 =QLabel(self)
        # self.lab1.setMaximumSize(400, 400)
        # self.lab1.setMinimumSize(400,400)
        img_path = 'icon/17.jpg'  # 图片路径
        self.lab1.setStyleSheet("QLabel{\n"
                               "border-image:url(\"%s\");\n"                       
                               "}" % img_path)
        self.lab1.move(0, 0)
        self.lab1.resize(800, 800)


        self.btn = QPushButton(self)
        self.btn.setToolTip("注册")
        self.btn.setMaximumSize(50,50)
        self.btn.setMinimumSize(50,50)
        img_path = 'icon/zhuce.png'#图片路径
        self.btn.setStyleSheet("QPushButton{\n"
                               "border-image:url(\"%s\");\n"
                               "}" % img_path)

        self.btn.move(300,500)


        self.btn1 = QPushButton(self)
        self.btn1.setToolTip("返回")
        self.btn1.setMaximumSize(50, 50)
        self.btn1.setMinimumSize(50, 50)
        img_path = 'icon/fanhui.png'  # 图片路径
        self.btn1.setStyleSheet("QPushButton{\n"
                               "border-image:url(\"%s\");\n"
                               "}" % img_path)
        self.btn1.move(430,500)

        self.label = QLabel(self)
        self.label.setText("用户名")
        self.label.setStyleSheet("QLabel{color:rgb(170,0,127,255);font-size:35px;font-weight:normal;font-family:Arial;}")
        self.label.move(110, 250)

        self.label1 = QLabel(self)
        self.label1.setText("密码")
        self.label1.setStyleSheet(
            "QLabel{color:rgb(170,0,127,255);font-size:35px;font-weight:normal;font-family:Arial;}")
        self.label1.move(110, 330)

        self.label2 = QLabel(self)
        self.label2.setText("确认密码")
        self.label2.setStyleSheet(
            "QLabel{color:rgb(170,0,127,255);font-size:35px;font-weight:normal;font-family:Arial;}")
        self.label2.move(110, 400)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setStyleSheet(
            "QLineEdit{font-size:35px;}")
        self.lineEdit.setFixedSize(300, 50)
        self.lineEdit.move(250,240)
        self.lineEdit.setFixedSize(350,50)

        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setStyleSheet(
            "QLineEdit{font-size:35px;}")
        rx= QRegExp("^[0-9A-Za-z]{8,18}$")
        self.lineEdit.setValidator(QRegExpValidator(rx,self))
        # regx = QLineEdit("^[0-9A-Za-z]{8,18}$")
        # validator = QLineEdit.(regx, self.lineEdit1)
      #  self.lineEdit1.setValidator(validator)

        self.lineEdit1.setFixedSize(300, 50)
        self.lineEdit1.move(250, 320)
        self.lineEdit1.setFixedSize(350, 50)
        self.lineEdit1.setEchoMode(QLineEdit.Password)

        self.lineEdit2 = QLineEdit(self)
        self.lineEdit2.setStyleSheet(
            "QLineEdit{font-size:35px;}")
        self.lineEdit2.setFixedSize(300, 50)
        self.lineEdit2.move(250, 390)
        self.lineEdit2.setFixedSize(350, 50)
        self.lineEdit2.setEchoMode(QLineEdit.Password)
        #img =cv2.imread('./1.jpg')
        self.btn.clicked.connect(self.codeRegister)
        self.btn1.clicked.connect(self.goback)

    def file_writer(self, file_path, user):
        with open(file_path, mode="a+") as file:
            file.write(user["name"] + "," + user["pwd"]+"\n")
        pass
    def file_read(self, file_path):
        with open(file_path,mode="r") as file:
            for line in file.readlines():
                line = line.strip()
                name,pwd = line.split(",")
                newuserdict = {"name": name,"pwd":pwd}
                self.users.append(newuserdict)
            return self.users
        pass

    def codeRegister(self):
        users = self.file_read(self.file_path)
        name = self.lineEdit.text()
        pwd = self.lineEdit1.text()
        supwd = self.lineEdit2.text()
        self.regFlag = True
        if name:
            #print(name)
            for i in range(0, len(users)):
                if name == list(users[i].values())[0]:
                    QMessageBox.warning(self, "警告", "存在同名用户，请重新输入新用户名")
                    self.regFlag = False
                    break
        else:
            QMessageBox.warning(self, "警告", "用户名不能为空")
            self.regFlag = False
        #print(self.regFlag)
        if self.regFlag:
            if pwd:
                if pwd == supwd:
                    newuserdict = {"name": name, "pwd": pwd}
                    self.file_writer("./registerInformation/users.txt", newuserdict)
                    QMessageBox.information(self, "信息", "恭喜你，注册成功")
                    winMa.login.show()
                    self.close()
                elif pwd != supwd:
                    QMessageBox.warning(self, "警告", "两次密码输入不匹配")
            else:
                QMessageBox.warning(self, "警告", "密码或确认密码不能为空")
        pass
    def goback(self):
        winMa.login.show()
        self.close()
if __name__ == "__main__":
    app=QApplication(sys.argv)
    #login = LoginWin()
    win =Register()
    win.show()
    sys.exit(app.exec_())

