#include "playwin.h"
#include<QMediaPlaylist>
#include"data.h"
#include <QKeyEvent>
#include <QMouseEvent>
#include <QApplication>
#include <QStyle>
int click = 0;
int i=0;
bool state_slider_volume = false;
Playwin::Playwin(QWidget *parent) : QWidget(parent)
{
    this->resize(1200,600);
    this->setStyleSheet("background-color:rgb(0,0,0)");
    QCursor cursor;
    cursor.setShape(Qt::OpenHandCursor);
    setCursor(cursor);

    player = new QMediaPlayer(this);
    //connect(player, &QMediaPlayer::positionChanged,this, &Playwin::updatePosition);
    VideoWidget =new QVideoWidget(this);
    player->setVideoOutput(VideoWidget);

    playBut = new QPushButton(this);
    videoSlider = new QSlider(Qt::Horizontal);
    videoSlider->installEventFilter(this);
    videoSlider->setMaximum(maxValue);
    timer = new QTimer();
    timer->setInterval(1000);
    timer->start();
    //将timer连接至onTimerOut槽函数
    connect(timer, SIGNAL(timeout()), this, SLOT(onTimerOut()));



    //playBut->setText("play");
    playBut->setMaximumSize(30,30);
    playBut->setMinimumSize(30,30);
    playBut->setStyleSheet(QStringLiteral("border-image:url(:/image/begin.png);"));
    QHBoxLayout *hlayout = new QHBoxLayout;
    hlayout->addWidget(playBut);

    QPushButton *pauseVideo= new QPushButton(this);
    pauseVideo->setMaximumSize(30,30);
    pauseVideo->setMinimumSize(30,30);
    pauseVideo->setStyleSheet(QStringLiteral("border-image:url(:/image/pause.png);"));
    hlayout->addWidget(pauseVideo);

    QPushButton *stopVideo= new QPushButton(this);
    stopVideo->setMaximumSize(30,30);
    stopVideo->setMinimumSize(30,30);
    stopVideo->setStyleSheet(QStringLiteral("border-image:url(:/image/stopcircle.png);"));
    hlayout->addWidget(stopVideo);

//    QPushButton *fullvideo = new QPushButton(this);
//    fullvideo->setMaximumSize(30,30);
//    fullvideo->setMinimumSize(30,30);
//    fullvideo->setStyleSheet(QStringLiteral("border-image:url(:/image/screenAmplify.png);"));
//    hlayout->addWidget(fullvideo);

    hlayout->addWidget(videoSlider);

    QVBoxLayout *vlayout = new QVBoxLayout(this);
    vlayout->addWidget(VideoWidget);
    vlayout->addLayout(hlayout);

    QHBoxLayout *hlayout2 =new QHBoxLayout;
    volumeSlider = new QSlider(this);
    volumeSlider->setOrientation(Qt::Vertical);
    volumeSlider->setEnabled(false);
    volumeSlider->hide();
    hlayout->addWidget(volumeSlider);

    connect(volumeSlider,SIGNAL(sliderPressed()),this,SLOT(slider_volume_changed()));
    connect(volumeSlider,SIGNAL(sliderMoved(int)),this,SLOT(slider_volume_changed()));

    //connect(fullvideo,SIGNAL(clicked(bool)),this,SLOT(full_clicked()));
    connect(stopVideo,SIGNAL(clicked(bool)),this,SLOT(stop_clicked()));
    connect(pauseVideo,SIGNAL(clicked(bool)),this,SLOT(pause_clicked()));
    connect(playBut,SIGNAL(clicked(bool)),this,SLOT(OpenVideoFile()));

    videoSlider->setEnabled(true);
    connect(videoSlider,SIGNAL(sliderPressed()),this,SLOT(slider_progress_clicked()));
    connect(videoSlider,SIGNAL(sliderMoved(int)),this,SLOT(slider_progress_moved()));
    connect(videoSlider,SIGNAL(sliderReleased()),this,SLOT(slider_progress_release()));

}

void Playwin::SetVideoUrl(const QUrl &url)
{
    player->setMedia(url);
   // SetVideoUrl(url);
    //  player->play();
}

void Playwin::slider_volume_changed()
{
    player->setVolume(volumeSlider->value());
}

void Playwin::OpenVideoFile()
{
//    QString filename = QFileDialog::getOpenFileName(this,"open video","./","video files(*.mp4)");
//    qDebug()<<filename;
//    SetVideoUrl(filename);
//    SetVideoUrl(Data::playpath);
    player->play();
}

void Playwin::on_horizontalSlider_sliderMoved(int position)
{
    player->setPosition(position * 1000);
}

void Playwin::updatePosition(qint64 position)
{
    videoSlider->setMaximum(player->duration() / 1000);
    videoSlider->setValue(position /1000);
}

void Playwin::pause_clicked()
{
    player->pause();
}

void Playwin::stop_clicked()
{
    player->stop();
}

void Playwin::full_clicked()
{

    VideoWidget->setWindowFlags (Qt::Window);
    VideoWidget->resize(1800,1000);
    VideoWidget->showFullScreen();
}

void Playwin::slider_progress_clicked()
{
    timer->stop();
    player->pause();
    player->setPosition(videoSlider->value()*player->duration()/maxValue );
    timer->start();
    player->play();
}

void Playwin::slider_progress_moved()
{
    timer->stop();
    player->pause();
    player->setPosition(videoSlider->value()*player->duration()/maxValue);
}

void Playwin::slider_progress_release()
{
    timer->start();
    player->play();
}

void Playwin::mousePressEvent(QMouseEvent *event)
{

    if(event->button() == Qt::LeftButton){
        QCursor cursor;
        cursor.setShape(Qt::ClosedHandCursor);
        offset=event->globalPos() - pos();
        i++;
        if(i%2==1)
        {
            timer->stop();
            player->pause();

        }else if (i%2==0){
            timer->start();
            player->play();
        }
        qDebug()<<i;
    }
}

void Playwin::mouseReleaseEvent(QMouseEvent *event)
{
    QApplication::restoreOverrideCursor();
}

void Playwin::mouseDoubleClickEvent(QMouseEvent *event)
{
    if(event->button()==Qt::LeftButton){
        if(windowState()==Qt::WindowFullScreen)
        {
            setWindowState(Qt::WindowNoState);
        }else setWindowState(Qt::WindowFullScreen);
    }

}

void Playwin::mouseMoveEvent(QMouseEvent *event)
{
    if(event->button() & Qt::LeftButton){
        QPoint temp;
        temp=event->globalPos() - offset;
        move(temp);
    }
}

void Playwin::wheelEvent(QWheelEvent *event)
{

}

//bool Playwin::eventFilter(QObject *obj, QEvent *event)
//{
//    if(obj == videoSlider){
//        if(event->type() == QEvent::MouseButtonPress){
//            QMouseEvent *mouseEvent = static_cast<QMouseEvent * >(event);
//            if(mouseEvent->button() == Qt::LeftButton){
//                int value = QStyle::sliderValueFromPosition(videoSlider->minimum(),videoSlider->maximum(),mouseEvent->pos().x(),videoSlider->width());
//                videoSlider->setValue(value);
//            }
//        }
//    }
//    return QObject::eventFilter(obj,event);
//}

void Playwin::onTimerOut()
{
    //qDebug()<<player->position()*maxValue/player->duration();
    videoSlider->setValue(player->position()*maxValue/player->duration());
}

void Playwin::on_pushButton_volume_clicked()
{
    if(volumeSlider)
    {
        volumeSlider->hide();
    }
    else
    {
        volumeSlider->setValue(player->volume());
        volumeSlider->setGeometry(QRect(volumeSlider->pos().rx()+0.5*volumeSlider->width()-15,volumeSlider->y()-100,30,102));
        volumeSlider->show();
    }
    state_slider_volume = !state_slider_volume;
}
