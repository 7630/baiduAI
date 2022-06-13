#include "data.h"
#include <QDebug>
#include "user.h"
#include<QList>
#include <QtGlobal>
QList <user *> Data::userlist;
QString Data::playpath;
Data::Data()
{
    user *u1 = new user("lili","123456");
    user *u2 = new user("admin","123456");
    user *u3 = new user("wyx","123456");
    user *u4 = new user("zkc","123456");

    Data::userlist.append(u1);
    Data::userlist.append(u2);
    Data::userlist.append(u3);
    Data::userlist.append(u4);
    qDebug()<<Data::userlist.size();
   // qDebug()<<qrand();
}
