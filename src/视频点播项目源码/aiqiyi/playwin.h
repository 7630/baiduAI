#ifndef PLAYWIN_H
#define PLAYWIN_H

#include <QWidget>
#include <QMediaPlayer>
#include <QVideoWidget>
#include <QPushButton>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QSlider>
#include <QFileDialog>
#include <QUrl>
#include <QKeyEvent>
#include <QMouseEvent>
#include <QEvent>
#include <QTimer>

namespace Ui {
class Playwin;
}
class Playwin : public QWidget
{
    Q_OBJECT
public:
    explicit Playwin(QWidget *parent = 0);
    QMediaPlayer *player;
    QVideoWidget *VideoWidget;

    QPushButton *playBut;
    QSlider *videoSlider;
    QSlider *volumeSlider;

    QKeyEvent *keyset;
    QTimer *timer;

    int maxValue = 1000;
    void SetVideoUrl(const QUrl &url);


    void mousePressEvent(QMouseEvent *event);
    void mouseReleaseEvent(QMouseEvent *event);
    void mouseDoubleClickEvent(QMouseEvent *event);
    void mouseMoveEvent(QMouseEvent *event);
    void wheelEvent(QWheelEvent *event);
 //   bool eventFilter(QObject *obj, QEvent *event);

    void on_pushButton_volume_clicked();
signals:

public slots:
    void OpenVideoFile();
    void on_horizontalSlider_sliderMoved(int position);
    void updatePosition(qint64 position);
    void pause_clicked();
    void stop_clicked();
    void full_clicked();
    void slider_progress_clicked();
    void slider_progress_moved();
    void slider_progress_release();
    void onTimerOut();
    void slider_volume_changed();
//protected:

private:
    QPoint offset;
};

#endif // PLAYWIN_H
