#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QList>
#include "user.h"

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = 0);
    ~Widget();

 //   QLabel *LabName;
 //   QList <user *> userlist;

public slots:
    void Gotoform();
    bool GetUserNameandPwd();
    void GotoMainWin();
private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
