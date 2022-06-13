#include "user.h"
#include <QString>

user::user()
{

}

user::user(QString username, QString userpwd)
{
    this->username = username;
    this->userpwd = userpwd;

}

QString user::GetUserName()
{
    return this->username;
}

QString user::GetUserPwd()
{
    return this->userpwd;
}
