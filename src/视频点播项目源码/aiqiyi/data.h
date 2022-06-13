#ifndef DATA_H
#define DATA_H
#include "user.h"
#include <QList>

class Data
{
public:
    Data();
    static QList <user *> userlist;
    static QString playpath;
};

#endif // DATA_H
