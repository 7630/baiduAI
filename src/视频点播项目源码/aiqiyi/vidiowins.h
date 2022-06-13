#ifndef VIDIOWINS_H
#define VIDIOWINS_H

#include <QWidget>
#include <QListWidgetItem>
#include "playwin.h"
#include <QListWidget>
namespace Ui {
class vidiowins;
}

class vidiowins : public QWidget
{
    Q_OBJECT

public:
    explicit vidiowins(QWidget *parent = 0);
    ~vidiowins();

    QString path;
    Playwin *pPlayWin;
    QListWidget *vidiowins1;
public slots:
    void skin();
    void getItemText(QListWidgetItem *item);
    void BtnSLot();

private:
    Ui::vidiowins *ui;
};

#endif // VIDIOWINS_H
