#include "widget.h"
#include <QApplication>
#include "form.h"
#include "dongtu.h"
#include "data.h"
#include "video.h"
#include "vidiowins.h"
#include "playwin.h"
class CommonHelper
{
    public:
    static void setStyle(const QString &style){
        QFile qss(style);
        qss.open(QFile::ReadOnly);
        qApp->setStyleSheet(qss.readAll());
        qss.close();
    }
};

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CommonHelper::setStyle("qss/style.qss");
    Widget w;
    Data *padata=new Data;
    w.show();

//   Playwin z;
//   z.show();
//    vidiowins y;
//    y.show();
    return a.exec();
}
