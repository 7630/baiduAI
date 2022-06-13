#include "form.h"
#include "ui_form.h"
#include "user.h"
#include <QString>
#include "data.h"
#include <QDebug>
#include <QMessageBox>
#include "widget.h"
#include "skip.h"
#include <QtGlobal>
Form::Form(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form)
{
    ui->setupUi(this);
    this->setWindowTitle("注册");
    skip::fo=this;
    connect(ui->pushButton,SIGNAL(clicked(bool)),this,SLOT(RegUserSlot()));
    connect(ui->pushButton_2,SIGNAL(clicked(bool)),this,SLOT(Goback()));
    int verify=qrand()%10000;
    QString verifyCode=QString::number(verify);
    ui->label_6->setText(verifyCode);

}

Form::~Form()
{
    delete ui;
}

bool Form::samename()
{
    QString username =ui->lineEdit->text();
   // QString pwd =ui->lineEdit_2->text();
    for(int i=0;i<Data::userlist.size();i++)
   {
     if(strcmp(username.toLatin1(),Data::userlist.at(i)->username.toLatin1() )==0)
     {
        return true;
     }
    }
        return false;
}

void Form::RegUserSlot()
{

    QString username =ui->lineEdit->text();
    QString userpwd = ui->lineEdit_2->text();
    QString userpwdsure = ui->lineEdit_3->text();
    QString verifytext = ui->lineEdit_4->text();

    if(ui->checkBox->isChecked()==false)
    {
       QMessageBox::warning(this, "注册提示","未勾选协议");
    }
    else if(username.isEmpty() || userpwd.isEmpty() || userpwdsure.isEmpty())
    {
       QMessageBox::warning(this, "注册提示","账号或密码空缺");
    }
    else if(userpwd!=userpwdsure)
      {
          QMessageBox::warning(this, "注册提示","确认密码错误");
      }
    else if(samename())
        {
           QMessageBox::warning(this, "注册提示","存在同名用户");
        }
        else if(verifytext!=ui->label_6->text())
        {
             QMessageBox::warning(this, "注册提示","验证码错误，重新输入");
             int verify=qrand()%10000;
             QString verifyCode=QString::number(verify);
             ui->label_6->setText(verifyCode);
        }
         else
        {
            //创建新节点
            user *newuser=new user(username,userpwd);
            Data::userlist.append(newuser);
            QMessageBox::information(this,"注册提示","注册成功");
            //qDebug() << Data::userlist.size();
            skip::wid->show();
            this->close();
        }

}

void Form::Goback()
{
    skip::wid->show();
    this->close();
}
