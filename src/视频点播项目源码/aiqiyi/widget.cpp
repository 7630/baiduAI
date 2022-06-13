#include "widget.h"
#include "ui_widget.h"
#include "form.h"
#include <QMovie>
#include <QDebug>
#include <QList>
#include <QMessageBox>
#include "dongtu.h"
#include "user.h"
#include "data.h"
#include "skip.h"
#include "vidiowins.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
    this->setWindowTitle("登录界面");
    QMovie *movie = new QMovie("image/bofa.gif");
    ui->label_4->setMovie(movie);
    ui->label_4->setMovie(movie);

    QSize size = ui->label_4->size();
    movie->setScaledSize(size);
    ui->label_4->setMovie(movie);
    movie->start();

    ui->lineEdit_2->setEchoMode(QLineEdit::Password);
    skip::wid=this;
    connect(ui->pushButton_2,SIGNAL(clicked(bool)),this,SLOT(Gotoform()));
    //connect(ui->pushButton,SIGNAL(clicked(bool)),this,SLOT(GetUserNameandPwd()));
    //QLabel label;
    connect(ui->pushButton,SIGNAL(clicked(bool)),this,SLOT(GotoMainWin()));
}

Widget::~Widget()
{
    delete ui;
}


void Widget::Gotoform()
{
    Form *pregwin = new Form;
    pregwin->show();
    this->hide();
}

bool Widget::GetUserNameandPwd()
{
    QString name = ui->lineEdit->text();
    QString pwd = ui->lineEdit_2->text();
    //qDebug()<<name;
    //qDebug()<<Data::userlist.at(1)->GetUserName().toLatin1();
    for(int i=0;i<Data::userlist.size();i++)
    {
        if(strcmp(name.toLatin1(),Data::userlist.at(i)->GetUserName().toLatin1() ) == 0 &&
                strcmp(pwd.toLatin1(),Data::userlist.at(i)->GetUserPwd().toLatin1() )==0)
        {
            //qDebug()<<"匹配成功";
//            QMessageBox msgBox;
//            msgBox.setText("登录成功.");
//            msgBox.exec();
            vidiowins *pregwin1 = new vidiowins;
            pregwin1->show();
            this->hide();
            return true;
        }

    }

}

void Widget::GotoMainWin()
{
    if(GetUserNameandPwd() == true)
    {
        QMessageBox::information(this,"登录提示","登录成功");

    }else {
        QMessageBox::information(this,"登录提示","密码错误");
     //  qDebug()<<"匹配失败";
    }
}
