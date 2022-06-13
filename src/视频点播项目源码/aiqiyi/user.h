#ifndef USER_H
#define USER_H

#include<QString>
class user
{
public:
    user();
    user(QString username,QString userpwd);
    QString username;
    QString userpwd;
    QString GetUserName();
    QString GetUserPwd();

};

#endif // USER_H
