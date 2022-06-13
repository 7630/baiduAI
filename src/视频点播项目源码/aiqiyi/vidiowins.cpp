#include "vidiowins.h"
#include "ui_vidiowins.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QPushButton>
#include <QDebug>
#include <QStringList>
#include <QListWidget>
#include <QDir>
#include <QTextCodec>
#include <QLineEdit>
#include <QLabel>
#include "playwin.h"
#include "data.h"

int clicktry=0;

vidiowins::vidiowins(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::vidiowins)
{
    ui->setupUi(this);
    this->setStyleSheet("background-color:rgb(0,0,0)");

    vidiowins1=new QListWidget(this);  //加图片

    vidiowins1->setIconSize(QSize(250,420));
    vidiowins1->setViewMode(QListView::IconMode);
    vidiowins1->setResizeMode(QListView::Adjust);
    vidiowins1->setMovement(QListView::Static);

    QWidget *window = new QWidget(this);//按钮跟着窗口一起伸缩放大加this
    QHBoxLayout *hlayout=new QHBoxLayout(this);
    //动态加载
    QVBoxLayout *vlayout = new QVBoxLayout();
    QStringList vidiolist;
    vidiolist<<"推荐"<<"恋恋剧场" <<"电视剧"<<"电影"<<"综艺"<<"动漫"<<"纪录片"<<"直播"<<"体育"<<"汽车"<<"母婴" ;

    QLabel *label = new QLabel(this);
    label->resize(300,100);
    label->setContentsMargins(10,10,10,10);
    //label->setGeometry(QRect(20,30,500,300));
    label->setStyleSheet(QStringLiteral("border-image: url(:/image/aiqiyi.png);"));
    label->setMaximumHeight(40);
    vlayout->addWidget(label);
    //vlayout->addStretch(1);
    for(int i = 0; i<vidiolist.size();++i)
    {
        //qDebug()<<vidiolist.at(i);
        QPushButton *newbutton =new QPushButton(vidiolist.at(i));
        connect(newbutton,SIGNAL(clicked(bool)),this,SLOT(BtnSLot()));
        newbutton->setObjectName("newbut");
        vlayout->addWidget(newbutton);

    }
   // vlayout->addStretch(1);

    //        QPushButton *surebut =new QPushButton("详细");
    //        surebut->setObjectName("newbut");
    //        vlayout->addWidget(surebut);

    QVBoxLayout *vlayout1 = new QVBoxLayout();
    QHBoxLayout *hlayout1 = new QHBoxLayout();
    QHBoxLayout *hlayout2 = new QHBoxLayout();
    QVBoxLayout *vlayout2 = new QVBoxLayout();

    QStringList videolist2;
    videolist2<<"搜索"<<"用户"<<"vip"<<"历史记录"<<"下载";
    hlayout2->addStretch(1);
    QLineEdit *LineEdit =new QLineEdit;
    LineEdit->setStyleSheet("background-color:white;");
    hlayout2->addWidget(LineEdit);
//    for(int i = 0;i<videolist2.size();++i)
//    {
//        QPushButton *newbutton2 =new QPushButton(videolist2.at(i));
//        hlayout2->addWidget(newbutton2);
//    }

    QPushButton *newbutton2 =new QPushButton("");
    newbutton2->setMaximumSize(30,30);
    newbutton2->setMinimumSize(30,30);
    newbutton2->setStyleSheet(QStringLiteral("border-image:url(:/image/sosuo.png);"));
    hlayout2->addWidget(newbutton2);

    QPushButton *newbutton3 =new QPushButton("");
    newbutton3->setMaximumSize(30,30);
    newbutton3->setMinimumSize(30,30);
    newbutton3->setStyleSheet(QStringLiteral("border-image:url(:/image/admin.png);"));
    hlayout2->addWidget(newbutton3);

    QPushButton *newbutton4 =new QPushButton("");
    newbutton4->setMaximumSize(30,30);
    newbutton4->setMinimumSize(30,30);
    newbutton4->setStyleSheet(QStringLiteral("border-image:url(:/image/VIP.png);"));
    hlayout2->addWidget(newbutton4);

    QPushButton *newbutton5 =new QPushButton("");
    newbutton5->setMaximumSize(30,30);
    newbutton5->setMinimumSize(30,30);
    newbutton5->setStyleSheet(QStringLiteral("border-image:url(:/image/history.png);"));
    hlayout2->addWidget(newbutton5);

    QPushButton *newbutton6 =new QPushButton("");
    newbutton6->setMaximumSize(30,30);
    newbutton6->setMinimumSize(30,30);
    newbutton6->setStyleSheet(QStringLiteral("border-image:url(:/image/down.png);"));
    hlayout2->addWidget(newbutton6);

    QPushButton *changecolor = new QPushButton("");
    changecolor->setMaximumSize(30,30);
    changecolor->setMinimumSize(30,30);
    changecolor->setStyleSheet(QStringLiteral("border-image:url(:/image/huanfu.png);"));
    hlayout2->addWidget(changecolor);

    connect(changecolor,SIGNAL(clicked(bool)),this,SLOT(skin()));


    QStringList videolist3;
    videolist3<<"排行榜"<<"1、变成你的那一天"<<"2、壮志高飞"<<"3、爱上特种兵"<<"4、理想照耀中国"<<"5、夜凛神探"<<"6、觉醒年代"<<"7、叛逆者"<<"8、恋爱生物钟" ;

    for(int i = 0;i<videolist3.size();++i)
    {
        QPushButton *newbutton3 = new QPushButton(videolist3.at(i));
        vlayout2->addWidget(newbutton3);
    }
 //   vlayout2->addStretch(1);

    hlayout->addLayout(vlayout);
    hlayout->addLayout(hlayout1);
    hlayout1->addLayout(vlayout1);
    hlayout1->addLayout(vlayout2);
    vlayout1->addLayout(hlayout2);
    vlayout1->addWidget(vidiowins1);

    //获取视频列表路径
    //QDir::currentPath()获取当前工程路径
    QString path=QString(QDir::currentPath()+"/"+"image"+"/"+"video");
    qDebug()<<path;
    QDir dir(path);  //打开文件夹

    QStringList namefiles;
    namefiles << QString("*.jpg");
    qDebug()<<namefiles;
    //读取文件名
    QStringList files= dir.entryList(namefiles,QDir::Files|QDir::Readable,QDir::Name);
    qDebug()<<files;
    for (int i=0;i<files.size();++i)
    {
        qDebug()<<files.at(i);
        //新建部件：图片加文本
        QStringList name = files.at(i).split(".");
        QListWidgetItem *newitem=new QListWidgetItem(QIcon(QPixmap(path+"/"+files.at(i))),name.at(0));
//        QFileInfo fi = files.at(i);
//        newitem->setText(fi.baseName());
        newitem->setSizeHint(QSize(250,420));
        vidiowins1->addItem(newitem);
    }

    connect(vidiowins1,SIGNAL(itemClicked(QListWidgetItem*)),this,SLOT(getItemText(QListWidgetItem *)));
}

vidiowins::~vidiowins()
{
    delete ui;
}

void vidiowins::skin()
{
    if(clicktry%2==0)
    {
        this->setStyleSheet("background-color: rgb(255, 255, 255)");
        this->setStyleSheet("color: black");
    }else
    {
        this->setStyleSheet("background-color: rgb(0, 0, 0)");
       // this->setStyleSheet("color: white");
    }
    clicktry++;
}

void vidiowins::getItemText(QListWidgetItem *item)
{
    QString itemtext=item->text();
   // qDebug()<<itemtext;
    QString videopath = QString("D:/Users/12466/Documents/build-aiqiyi-Desktop_Qt_5_8_0_MinGW_32bit-Debug/image/MP4/"+itemtext+".mp4");

    //QString videopath = QString(QDir::currentPath()+"/MP4/"+itemtext+".mp4");

    qDebug()<<videopath;
    pPlayWin = new Playwin;
    pPlayWin->SetVideoUrl(videopath);
    pPlayWin->show();

     // pPlayWin->player->play();
//    Data::playpath = QString(QDir::currentPath()+"/MP4/"+itemtext+".mp4");

//    Playwin *play = new Playwin;
//    play->show();
}

void vidiowins::BtnSLot()
{
    QPushButton *btn = (QPushButton *)sender();
    if(btn->text()=="电影")
    {
        vidiowins1->clear();
        QString path=QString(QDir::currentPath()+"/"+"image"+"/"+"video"+"/"+"film");
        qDebug()<<path;
        QDir dir(path);  //打开文件夹

        QStringList namefiles;
        namefiles << QString("*.jpg");
        qDebug()<<namefiles;
        //读取文件名
        QStringList files= dir.entryList(namefiles,QDir::Files|QDir::Readable,QDir::Name);
        qDebug()<<files;
        for (int i=0;i<files.size();++i)
        {
            qDebug()<<files.at(i);
            //新建部件：图片加文本
            QStringList name = files.at(i).split(".");
            QListWidgetItem *newitem=new QListWidgetItem(QIcon(QPixmap(path+"/"+files.at(i))),name.at(0));
            newitem->setSizeHint(QSize(250,420));
            vidiowins1->addItem(newitem);
        }
    }
    else if(btn->text()=="电视剧")
    {
        vidiowins1->clear();
        QString path=QString(QDir::currentPath()+"/"+"image"+"/"+"video"+"/"+"teleplay");
        qDebug()<<path;
        QDir dir(path);  //打开文件夹

        QStringList namefiles;
        namefiles << QString("*.jpg");
        qDebug()<<namefiles;
        //读取文件名
        QStringList files= dir.entryList(namefiles,QDir::Files|QDir::Readable,QDir::Name);
        qDebug()<<files;
        for (int i=0;i<files.size();++i)
        {
            qDebug()<<files.at(i);
            //新建部件：图片加文本
            QStringList name = files.at(i).split(".");
            QListWidgetItem *newitem=new QListWidgetItem(QIcon(QPixmap(path+"/"+files.at(i))),name.at(0));
            newitem->setSizeHint(QSize(250,420));
            vidiowins1->addItem(newitem);
        }
    }
    else{
        vidiowins1->clear();
        QString path=QString(QDir::currentPath()+"/"+"image"+"/"+"video");
        qDebug()<<path;
        QDir dir(path);  //打开文件夹

        QStringList namefiles;
        namefiles << QString("*.jpg");
        qDebug()<<namefiles;
        //读取文件名
        QStringList files= dir.entryList(namefiles,QDir::Files|QDir::Readable,QDir::Name);
        qDebug()<<files;
        for (int i=0;i<files.size();++i)
        {
            qDebug()<<files.at(i);
            //新建部件：图片加文本
            QStringList name = files.at(i).split(".");
            QListWidgetItem *newitem=new QListWidgetItem(QIcon(QPixmap(path+"/"+files.at(i))),name.at(0));
            newitem->setSizeHint(QSize(250,420));
            vidiowins1->addItem(newitem);
        }
    }
    qDebug()<<btn->text();
}

