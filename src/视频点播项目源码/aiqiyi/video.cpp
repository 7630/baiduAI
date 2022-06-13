#include "video.h"
#include "ui_video.h"
#include <QStringList>
#include <QDebug>

//布局管理器
Video::Video(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Video)
{
    ui->setupUi(this);


    QWidget *window = new QWidget(this);

   //设置布局
    QHBoxLayout *wlayout =new QHBoxLayout;
    QVBoxLayout *layout = new QVBoxLayout;
    QHBoxLayout *hlayout = new QHBoxLayout;

    //一个大的水平布局中加入一个垂直布局
     wlayout->addStretch(1);
     wlayout->addLayout(layout);
     layout->addStretch(1);
    //再加一个垂直布局layout1
     QVBoxLayout *layout1 = new QVBoxLayout;
     wlayout->addStretch(1);
     wlayout->addLayout(layout1);
     layout->addStretch(1);
     //往layout1中加入水平布局1
     layout1->addStretch(1);
     layout1->addLayout(hlayout);
     hlayout->addStretch(1);
     layout1->addStretch(1);
     //往layout1在再加入水平布局2
     QHBoxLayout *hlayout2 = new QHBoxLayout;

     layout1->addStretch(1);
     layout1->addLayout(hlayout2);
     hlayout2->addStretch(1);
     layout1->addStretch(1);

     //往水平布局2中加入一个垂直布局
    // QPushButton *button5 = new QPushButton("Five");
     QVBoxLayout *layout2 = new QVBoxLayout;
     //layout2->addWidget(button5);
     hlayout2->addStretch(1);
     hlayout2->addLayout(layout2);
     layout2->addStretch(1);
     hlayout2->addStretch(1);
     //往layout1再加一个水平布局3
     QHBoxLayout *hlayout3 = new QHBoxLayout;

     layout1->addStretch(1);
     layout1->addLayout(hlayout3);
     hlayout3->addStretch(1);
     layout1->addStretch(1);

   //放按钮
    QStringList fonts;
    fonts <<"教育"<<"直播"<<"娱乐"<<"搞笑"<<"游戏"<<"资讯"<<"片花"<<"音乐"<<"汽车"<<"军事"<<"母婴"<<"健康";
    for(int i = 0;i<fonts.size();++i)
    {
        qDebug()<<fonts.at(i);
        QPushButton *newbutton = new QPushButton(fonts.at(i));
        layout->addWidget(newbutton);
    }

    QStringList fonts1;
    fonts1 << "做家务的男人3"<<"变成你的那一天"<<"爱上特种兵"<<"叛逆者";
    for(int i=0;i<fonts1.size();++i)
    {
        qDebug()<<fonts1.at(i);
        QPushButton *newbuttonl = new QPushButton(fonts1.at(i));
        layout2->addWidget(newbuttonl);
    }


//    QPushButton *button1 = new QPushButton("One");
//    QPushButton *button2 = new QPushButton("Two");
//    QPushButton *button3 = new QPushButton("Three");
//    QPushButton *button4 = new QPushButton("Four");
//    QPushButton *button5 = new QPushButton("Five");
//    QPushButton *button6 = new QPushButton("six");
//    QPushButton *button7 = new QPushButton("seven");
//    QPushButton *button8 = new QPushButton("eight");
//    QPushButton *button9 = new QPushButton("nine");
//    QPushButton *button10 = new QPushButton("ten");

//    QPushButton *hbutton1 = new QPushButton("One");
//    QPushButton *hbutton2 = new QPushButton("Two");
//    QPushButton *hbutton3 = new QPushButton("Three");
//    QPushButton *hbutton4 = new QPushButton("Four");
//    QPushButton *hbutton5 = new QPushButton("Five");
//    QPushButton *h2button1 = new QPushButton("Five");
//    QPushButton *h3button1 = new QPushButton("Five");




//    //创建按键
//    layout->addWidget(button1);
//    layout->addWidget(button2);
//    layout->addWidget(button3);
//    layout->addWidget(button4);
//    layout->addWidget(button5);
//    layout->addWidget(button6);
//    layout->addWidget(button7);
//    layout->addWidget(button8);
//    layout->addWidget(button9);
//    layout->addWidget(button10);

//   //水平按键
//    hlayout->addWidget(hbutton1);
//    hlayout->addWidget(hbutton2);
//    hlayout->addWidget(hbutton3);
//    hlayout->addWidget(hbutton4);
//    hlayout->addWidget(hbutton5);

//    //window->setLayout(layout);
////   layout->addStretch(1);
////   hlayout->addLayout(layout);
////    hlayout->addStretch(1);

//hlayout2->addWidget(h2button1);//仅为了显示
// hlayout3->addWidget(h3button1);//仅为了显示

    window->setLayout(wlayout);
    window->show();
}

Video::~Video()
{
    delete ui;
}
